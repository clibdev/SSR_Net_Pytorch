# Fork of [oukohou/SSR_Net_Pytorch](https://github.com/oukohou/SSR_Net_Pytorch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/SSR_Net_Pytorch/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name    | Train                                              | Valid                                            | Test                                              | Link                                                                                                                                                                                                                                                                                                                         |
|---------|----------------------------------------------------|--------------------------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SSR-Net | Train Loss: 2.9401<br>CA_3: 0.6326<br>CA_5: 0.8123 | Val Loss: 4.7221<br>CA_3: 0.4438<br>CA_5: 0.6295 | Test Loss: 3.9311<br>CA_3: 0.5151<br>CA_5: 0.7163 | [PyTorch](https://github.com/clibdev/SSR_Net_Pytorch/releases/latest/download/model_Adam_MSELoss_LRDecay_weightDecay0.0001_batch50_lr0.0005_epoch90_64x64.pth), [ONNX](https://github.com/clibdev/SSR_Net_Pytorch/releases/latest/download/model_Adam_MSELoss_LRDecay_weightDecay0.0001_batch50_lr0.0005_epoch90_64x64.onnx) |

Note: results on MegaAge_Asian dataset.

# Inference

```shell
python inference_images.py --graph pretrained_model/model_Adam_MSELoss_LRDecay_weightDecay0.0001_batch50_lr0.0005_epoch90_64x64.pth --image data/images/88_megaage_asian_32_age.jpg
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py --weights pretrained_model/model_Adam_MSELoss_LRDecay_weightDecay0.0001_batch50_lr0.0005_epoch90_64x64.pth
```
