# -*-coding=utf-8 -*-
# @Time:2022/9/29 21:52
# @Author:姚昕成
# @File:tensor_tb.py
# @Software:PyCharm

from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = "D:/Pycharm2022/srtp/pictures/0190706.jpeg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)

writer.add_image("test", img_array, 2, dataformats="HWC")
for i in range(100):
    writer.add_scalar("y=2x", 3*i, i)

writer.close()