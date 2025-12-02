#!/usr/bin/env python3
"""Utility to pull trained weights from Google Drive into the local models/ folder."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

try:
    import gdown  # type: ignore
except ImportError as exc:  # pragma: no cover - handled by runtime guard
    raise SystemExit(
        "gdown is required for sync_models.py. Install dependencies via 'pip install -r requirements.txt'."
    ) from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download trained models listed in model_manifest.json from Google Drive",
    )
    parser.add_argument(
        "--manifest",
        default="model_manifest.json",
        type=Path,
        help="Path to the manifest JSON file (default: %(default)s)",
    )
    parser.add_argument(
        "--models-dir",
        default=Path("models"),
        type=Path,
        help="Directory where checkpoints will be stored (default: %(default)s)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download files even if they already exist",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the actions without downloading",
    )
    return parser.parse_args()


def compute_sha256(path: Path) -> str:
    hash_obj = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


def should_download(target: Path, expected_hash: Optional[str], force: bool) -> bool:
    if force:
        return True
    if not target.exists():
        return True
    if not expected_hash:
        return False
    return compute_sha256(target).lower() != expected_hash.lower()


def download_file(file_id: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url=url, output=str(destination), quiet=False)


def validate_manifest_entry(entry: Dict[str, str]) -> None:
    if "file_id" not in entry or "filename" not in entry:
        raise ValueError("Each manifest entry must contain 'file_id' and 'filename'.")
    if not entry["file_id"].strip():
        raise ValueError("Manifest 'file_id' cannot be empty.")
    if not entry["filename"].strip():
        raise ValueError("Manifest 'filename' cannot be empty.")


def load_manifest(manifest_path: Path) -> List[Dict[str, str]]:
    with manifest_path.open("r", encoding="utf-8") as manifest_file:
        data = json.load(manifest_file)
    models = data.get("models", [])
    if not isinstance(models, list):
        raise ValueError("Manifest 'models' key must contain a list.")
    return models


def main() -> None:
    args = parse_args()
    manifest_path = args.manifest
    models_dir: Path = args.models_dir

    if not manifest_path.exists():
        raise SystemExit(f"Manifest not found: {manifest_path}")

    manifest_entries = load_manifest(manifest_path)
    if not manifest_entries:
        print("No entries found in manifest; nothing to download.")
        return

    for entry in manifest_entries:
        validate_manifest_entry(entry)
        file_id = entry["file_id"].strip()
        filename = entry["filename"].strip()
        expected_hash = entry.get("sha256", "").strip() or None
        destination = models_dir / filename

        if args.dry_run:
            action = "would download" if should_download(destination, expected_hash, args.force) else "skip"
            print(f"[DRY-RUN] {action} {filename} -> {destination}")
            continue

        if not should_download(destination, expected_hash, args.force):
            print(f"Skipping {filename}: already present and matches expected hash.")
            continue

        if destination.exists() and args.force:
            destination.unlink()

        print(f"Downloading {filename} to {destination}...")
        download_file(file_id, destination)

        if not destination.exists():
            raise SystemExit(f"Failed to download {filename}.")

        if expected_hash:
            actual_hash = compute_sha256(destination)
            if actual_hash.lower() != expected_hash.lower():
                destination.unlink(missing_ok=True)
                raise SystemExit(
                    f"Hash mismatch for {filename}: expected {expected_hash}, got {actual_hash}. File removed."
                )
            print(f"Verified SHA-256 for {filename}.")

    print("Model sync complete.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # pragma: no cover - CLI entry point
        raise SystemExit(str(error))
