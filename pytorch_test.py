# -*-coding=utf-8 -*-
# @Time:2022/9/13 22:41
# @Author:姚昕成
# @File:pytorch_test.py
# @Software:PyCharm
import matplotlib.pyplot
import matplotlib.pyplot as plt
import torch
import torchvision
import pylab

model = torchvision.models.resnet18(pretrained=True)

from PIL import Image
import numpy as np

x = Image.open('D:/Pycharm2022/srtp/pictures/9850132.jpeg')
x = torch.tensor(np.array(x, 'float32') / 255-0.5)
x = x[:224, :224, :]
x = torch.permute(x, [2, 0, 1])
x = x[None, :, :, :]
x.requires_grad = True
lr = 1
for i in range(10):
    x.requires_grad = True
    y = model(x)
    loss = torch.mean(y[:, 248])
    loss.backward()
    grad = x.grad[:, :, :, :]
    with torch.no_grad():
        x = x - grad*lr

x = torch.permute(x[0], [1, 2, 0])
x = x.numpy() + 0.5
x = np.clip(x, 0, 1)
plt.imshow(x)