import argparse
import os
import torch
from SSR_models.SSR_Net_model import SSRNet


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--weights', type=str, default='./pretrained_model/model_Adam_MSELoss_LRDecay_weightDecay0.0001_batch50_lr0.0005_epoch90_64x64.pth', help='Weights path')
    parser.add_argument('--device', default='cpu', type=str, help='cuda:0 or cpu')
    args = parser.parse_args()

    if not os.path.exists(args.weights):
        print('Cannot find weights: {0}'.format(args.weights))
        exit()

    model = SSRNet()
    weights = torch.load(args.weights)
    model.load_state_dict(weights['state_dict'])
    model = model.to(args.device)
    model.eval()

    model_path = os.path.splitext(args.weights)[0] + '.onnx'
    print(model_path)

    dummy_input = torch.randn(1, 3, 64, 64).to(args.device)
    torch.onnx.export(
        model,
        dummy_input,
        model_path,
        verbose=False,
        input_names=['input'],
        output_names=['output'],
        opset_version=18
    )
