import torch
import transformers
import pandas as pd

print("=" * 50)
print("Environment Check")
print("=" * 50)

print("Python      :", __import__("sys").version)
print("PyTorch     :", torch.__version__)
print("Transformers:", transformers.__version__)
print("Pandas      :", pd.__version__)
print("CUDA Ready  :", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU         :", torch.cuda.get_device_name(0))
else:
    print("GPU         : Tidak terdeteksi (CPU Mode)")