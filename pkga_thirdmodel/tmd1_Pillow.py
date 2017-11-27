#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用第三方模块(1)
# 图像处理框架 Pillow

# 快速打印
from util import p
from PIL import Image, ImageFilter
from PIL import ImageDraw, ImageFont
import random

# 读取图片至对象
img = Image.open('../assets/yellow.jpg')
w, h = img.size
p('图片宽高：%s x %s' % (w, h))
# 生成宽高减半的图片对象
img.thumbnail((w // 2, h // 2))
p('缩小后宽高：%s x %s' % (w // 2, h // 2))
# 保存图片对象
img.save('../assets/yellow2.jpg', 'jpeg')

img2 = Image.open('../assets/yellow2.jpg')
# 添加滤镜生成新图片对象
img3 = img2.filter(ImageFilter.BLUR)
# 保存图片
img2.save("../assets/yellowblur.jpg")

# --------生成图片


def rand_chr():
    return chr(random.randint(65, 90))


def rand_color():
    tp = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    return tp


def rand_clr2():
    tp = (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    return tp


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('../assets/newfont.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rand_color())

for z in range(4):
    draw.text((60 * z + 10, 10), rand_chr(), font=font, fill=rand_clr2())

image = image.filter(ImageFilter.BLUR)
image.save('../assets/code.jpg', 'jpeg')



