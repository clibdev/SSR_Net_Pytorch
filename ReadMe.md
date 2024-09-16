# Fork of [oukohou/SSR_Net_Pytorch](https://github.com/oukohou/SSR_Net_Pytorch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.4. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/SSR_Net_Pytorch/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.
* The following deprecations has been fixed:
  * FutureWarning: You are using 'torch.load' with 'weights_only=False'.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

* Download links:

| Name    | Model Size (MB) | Link                                                                                                                                                                                 | SHA-256                                                                                                                              |
|---------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| SSR-Net | 0.6<br>0.2      | [PyTorch](https://github.com/clibdev/SSR_Net_Pytorch/releases/latest/download/ssr-net.pth), [ONNX](https://github.com/clibdev/SSR_Net_Pytorch/releases/latest/download/ssr-net.onnx) | bcf6d1413f9b0e70095eb20b5d95e3d13e1e73ad8c1585a62278c170bcfeda4c<br>5e97869699ce0d7b9a3c1fbf034011f140cf61ba037d37ead96d1740c1ed7a88 |

* Evaluation results on MegaAge_Asian dataset:

| Name    | Train                                              | Valid                                            | Test                                              |
|---------|----------------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| SSR-Net | Train Loss: 2.9401<br>CA_3: 0.6326<br>CA_5: 0.8123 | Val Loss: 4.7221<br>CA_3: 0.4438<br>CA_5: 0.6295 | Test Loss: 3.9311<br>CA_3: 0.5151<br>CA_5: 0.7163 |

# Inference

```shell
python inference_images.py --graph ssr-net.pth --image data/images/88_megaage_asian_32_age.jpg
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py --weights ssr-net.pth
```
