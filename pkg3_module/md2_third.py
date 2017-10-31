#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 模块 （2）
# 第三方模块

# PIL 库下载来源： pip install Pillow
from PIL import Image

img = Image.open('../assets/icon_boy.png')
print(img.format, img.size, img.mode)
img.thumbnail((120, 120))
img.save('../assets/icon_boy2.png', 'PNG')


