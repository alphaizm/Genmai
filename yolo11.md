# 環境構築
```
python -m venv .env
```

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
1.
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

2.
pip install torch==2.4.0+cu124 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu124

3.
pip install torch==2.5.1+cu124 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu124
```

## YOLO11でのモデル精度検証
https://docs.ultralytics.com/ja/usage/cli/#how-can-i-validate-the-accuracy-of-a-trained-yolo11-model-using-the-cli
```
yolo val model=yolo11n.pt data=coco8.yaml batch=1 imgsz=640
```

### エラー発生
> NotImplementedError: Could not run 'torchvision::nms' with arguments from the 'CUDA' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using custom build). If you are a Facebook employee using PyTorch on mobile, please visit https://fburl.com/ptmfixes for possible resolutions. 'torchvision::nms' is only available for these backends: [CPU, Meta, QuantizedCPU, BackendSelect, Python, FuncTorchDynamicLayerBackMode, Functionalize, Named, Conjugate, Negative, ZeroTensor, ADInplaceOrView, AutogradOther, AutogradCPU, AutogradCUDA, AutogradXLA, AutogradMPS, AutogradXPU, AutogradHPU, AutogradLazy, AutogradMeta, Tracer, AutocastCPU, AutocastXPU, AutocastMPS, AutocastCUDA, FuncTorchBatched, BatchedNestedTensor, FuncTorchVmapMode, Batched, VmapMode, FuncTorchGradWrapper, PythonTLSSnapshot, FuncTorchDynamicLayerFrontMode, PreDispatch, PythonDispatcher].

### 以下をためす
[YOLOv8でのエラー(Could not run 'torchvision::nms' with arguments from the 'CUDA' backend.)を解決](https://qiita.com/minti36/items/71768b20fdfc36b86e34)

```
pip list
```
↓
1.
```
torch              2.5.1+cu124
torchaudio         2.5.1+cu124
torchvision        0.20.1　// ★★★
```

2.
```
torch              2.4.0+cu124
torchaudio         2.4.0+cu124
torchvision        0.19.0+cu124
```
