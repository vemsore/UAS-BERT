"""
========================================================
DOWNLOAD MODEL FROM HUGGINGFACE
========================================================
"""

from pathlib import Path

from huggingface_hub import snapshot_download

from app.config import (
    HF_REPO_ID,
    MODEL_LOCAL_DIR,
)


def download_model():

    model_path = Path(MODEL_LOCAL_DIR)

    if model_path.exists():

        print("=" * 60)
        print("MODEL SUDAH ADA")
        print(model_path)
        print("=" * 60)

        return str(model_path)

    print("=" * 60)
    print("DOWNLOAD MODEL")
    print("=" * 60)

    snapshot_download(

        repo_id=HF_REPO_ID,

        repo_type="model",

        local_dir=model_path,

    )

    print()

    print("=" * 60)
    print("DOWNLOAD SELESAI")
    print(model_path)
    print("=" * 60)

    return str(model_path)


if __name__ == "__main__":

    download_model()