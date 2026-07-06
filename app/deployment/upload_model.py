from huggingface_hub import HfApi

api = HfApi()

api.upload_folder(
    folder_path="model/best_model",
    repo_id="Avemsoer/indobert-sentiment",
    repo_type="model",
)