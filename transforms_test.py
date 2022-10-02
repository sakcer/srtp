# -*-coding=utf-8 -*-
# @Time:2022/9/30 21:31
# @Author:姚昕成
# @File:transforms_test.py
# @Software:PyCharm

from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path = "D:/Pycharm2022/srtp/pictures/0066849.jpeg"

writer = SummaryWriter("logs")

img = Image.open(img_path)
tensors_trans = transforms.ToTensor()
tensor_img = tensors_trans(img)

writer.add_image("Tensor_img", tensor_img)

writer.close()