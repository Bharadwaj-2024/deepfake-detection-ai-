from django.shortcuts import render, redirect
from django.contrib import messages
import torch
from torchvision import transforms
from torch.utils.data.dataset import Dataset
import os
import numpy as np
import cv2
from torch import nn
import glob
import shutil
from django.conf import settings
from .forms import VideoUploadForm
import face_recognition
import time
from .models import DeepfakeModel


# --------------------------- DEVICE SETUP --------------------------- #
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("\n🔥 Running on:", device, "\n")


# --------------------------- CONSTANTS ------------------------------ #
index_template_name = 'index.html'
predict_template_name = 'predict.html'
about_template_name = "about.html"

im_size = 112
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
sm = nn.Softmax(dim=1)

train_transforms = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((im_size, im_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean, std)
])


# ---------------------- DATASET LOADER CLASS ------------------------ #
class validation_dataset(Dataset):
    def __init__(self, video_names, sequence_length=60, transform=None):
        self.video_names = video_names
        self.transform = transform
        self.count = sequence_length

    def __len__(self):
        return len(self.video_names)

    def __getitem__(self, idx):
        video_path = self.video_names[idx]
        frames = []

        for frame in self.frame_extract(video_path):
            faces = face_recognition.face_locations(frame)

            try:
                top, right, bottom, left = faces[0]
                frame = frame[top:bottom, left:right, :]
            except:
                pass

            frames.append(self.transform(frame))
            if len(frames) == self.count:
                break

        frames = torch.stack(frames)[:self.count]
        return frames.unsqueeze(0)

    def frame_extract(self, path):
        vid = cv2.VideoCapture(path)
        while True:
            success, image = vid.read()
            if not success:
                break
            yield image


# ---------------------- UTILITY FUNCTIONS --------------------------- #
def predict(model, img):
    _, logits = model(img.to(device))
    logits = sm(logits)
    _, pred = torch.max(logits, 1)
    confidence = float(logits[0][pred.item()] * 100)
    return int(pred.item()), confidence


def get_accurate_model(sequence_length):
    models_dir = os.path.join(settings.BASE_DIR, "ml_app", "ml_models")

    if not os.path.isdir(models_dir):
        raise ValueError(f"❌ Models folder missing at: {models_dir}")

    model_files = glob.glob(os.path.join(models_dir, "*.pt"))
    match = []

    for m in model_files:
        parts = os.path.basename(m).replace(".pt", "").split("_")
        try:
            acc = float(parts[1])
            seq = int(parts[3])
            if seq == sequence_length:
                match.append((acc, m))
        except:
            continue

    if not match:
        raise ValueError(f"❌ No matching model found for sequence length {sequence_length}")

    match.sort(reverse=True)
    print(f"✔ Selected model: {match[0][1]}")
    return match[0][1]



def allowed_video_file(filename):
    return filename.split('.')[-1].lower() in ['mp4','gif','webm','avi','3gp','wmv','flv','mkv']


# ---------------------------- VIEWS --------------------------------- #
def index(request):
    if request.method == "GET":
        form = VideoUploadForm()
        request.session.pop("file_name", None)
        request.session.pop("sequence_length", None)
        return render(request, index_template_name, {"form": form})

    form = VideoUploadForm(request.POST, request.FILES)

    if form.is_valid():
        video = form.cleaned_data['upload_video_file']
        seq_len = form.cleaned_data['sequence_length']

        if seq_len <= 0:
            form.add_error("sequence_length", "Sequence length must be > 0")
            return render(request, index_template_name, {"form": form})

        if not allowed_video_file(video.name):
            form.add_error("upload_video_file", "Unsupported video type")
            return render(request, index_template_name, {"form": form})

        saved_name = f"uploaded_{int(time.time())}.{video.name.split('.')[-1]}"
        save_path = os.path.join(settings.PROJECT_DIR, "uploaded_videos", saved_name)

        with open(save_path, 'wb') as out:
            shutil.copyfileobj(video, out)

        request.session["file_name"] = save_path
        request.session["sequence_length"] = seq_len

        return redirect('ml_app:predict')

    return render(request, index_template_name, {"form": form})


def predict_page(request):
    if 'file_name' not in request.session:
        return redirect("ml_app:home")

    video = request.session["file_name"]
    seq_len = request.session["sequence_length"]
    dataset = validation_dataset([video], seq_len, train_transforms)

    try:
        model_path = get_accurate_model(seq_len)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect("ml_app:home")

    model = DeepfakeModel(num_classes=2).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()

    label, conf = predict(model, dataset[0])
    result = "REAL" if label == 1 else "FAKE"

    return render(request, predict_template_name, {
        "output": result,
        "confidence": round(conf, 2),
        "video_name": os.path.basename(video)
    })


def about(request):
    return render(request, about_template_name)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def cuda_full(request):
    return render(request, 'cuda_full.html')
