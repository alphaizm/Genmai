# 環境構築
python -m venv .env 

# CUDAのバージョン確認
```
nvidia-smi
```
```
+-----------------------------------------------------------------------------------------+  
| NVIDIA-SMI 560.94                 Driver Version: 560.94         CUDA Version: 12.6     |  
|-----------------------------------------+------------------------+----------------------+  
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |  
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |  
|                                         |                        |               MIG M. |  
|=========================================+========================+======================|  
|   0  NVIDIA GeForce RTX 2070 ...  WDDM  |   00000000:01:00.0 Off |                  N/A |  
| N/A   38C    P0             18W /   80W |       0MiB /   8192MiB |      0%      Default |  
|                                         |                        |                  N/A |  
+-----------------------------------------+------------------------+----------------------+  
  
+-----------------------------------------------------------------------------------------+  
| Processes:                                                                              |  
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |  
|        ID   ID                                                               Usage      |  
|=========================================================================================|  
|  No running processes found                                                             |  
+-----------------------------------------------------------------------------------------+ 
```

# Yolo11
## ultralytics
https://github.com/ultralytics/ultralytics  
https://docs.ultralytics.com/ja/quickstart/#install-ultralytics

```
pip install ultralytics
```

## PyTorch
https://pytorch.org/get-started/locally/


PyTorch Build : Stable (2.5.1)  
OS : Windows  
Package : Pip  
Language : Python  
Compute Platform : CUDA 12.4  
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
