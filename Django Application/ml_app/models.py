"""
Models module for ml_app. Torch and torchvision imports are optional at import
time to allow the Django dev server to start on systems without heavy ML
dependencies installed (for previewing the site). If `torch` is not
available, `DeepfakeModel` is defined as a placeholder that raises a clear
error when instantiated.
"""

try:
    import torch
    import torch.nn as nn
    from torchvision import models
except Exception:
    torch = None
    nn = None
    models = None


if torch is not None:
    class DeepfakeModel(nn.Module):

        def __init__(self, num_classes, latent_dim=2048, lstm_layers=1, hidden_dim=2048, bidirectional=False):
            super(DeepfakeModel, self).__init__()

            # Pretrained ResNeXt model
            base_model = models.resnext50_32x4d(weights="IMAGENET1K_V1")

            # Remove last two layers (adaptive pooling + FC)
            self.model = nn.Sequential(*list(base_model.children())[:-2])

            # LSTM part
            self.lstm = nn.LSTM(latent_dim, hidden_dim, lstm_layers, bidirectional)

            # Classification layer (This name MUST match saved model key `linear1`)
            self.linear1 = nn.Linear(hidden_dim, num_classes)

            # Adaptive pooling layer
            self.avgpool = nn.AdaptiveAvgPool2d(1)

            self.dropout = nn.Dropout(0.4)
            self.relu = nn.LeakyReLU()

        def forward(self, x):
            batch_size, seq_len, c, h, w = x.shape

            # Reshape sequence for CNN
            x = x.view(batch_size * seq_len, c, h, w)

            fmap = self.model(x)
            x = self.avgpool(fmap)
            x = x.view(batch_size, seq_len, -1)

            lstm_out, _ = self.lstm(x, None)
            logits = self.dropout(self.linear1(lstm_out[:, -1, :]))

            return fmap, logits
else:
    class DeepfakeModel:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("DeepfakeModel requires 'torch' and 'torchvision'. "
                               "Install the ML dependencies or run the site without ML features.")
