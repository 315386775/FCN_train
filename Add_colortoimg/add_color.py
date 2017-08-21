#!usr/bin/python
# -*- coding:utf-8 -*-
import PIL.Image
import numpy as np
from skimage import io,data,color
import matplotlib.pyplot as plt

img = PIL.Image.open('xxx.png')
img = np.array(img)
dst = color.label2rgb(img, bg_label=0, bg_color=(0, 0, 0))
io.imsave('xxx.png', dst)