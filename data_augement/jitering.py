#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import os
from PIL import Image,ImageOps
import argparse
import random
from scipy import misc
import glob


def pcaCreate(image_files,dir,name_num, dir_list):
    image_list = []
    new_file_name = dir
    save_dir = dir_list + new_file_name
    save_dir_tt = save_dir + "\\"
    for image_file in image_files:
        image_list.append(misc.imread(image_file))

    for image in image_list:
        img = np.asarray(image, dtype='float32')
        img = img / 255.
        img_size = img.size / 3
        img1 = img.reshape(img_size, 3)
        img1 = np.transpose(img1)
        img_cov = np.cov([img1[0], img1[1], img1[2]])
        lamda, p = np.linalg.eig(img_cov)

        p = np.transpose(p)

        alpha1 = random.normalvariate(0, 0.3)
        alpha2 = random.normalvariate(0, 0.3)
        alpha3 = random.normalvariate(0, 0.3)
        v = np.transpose((alpha1 * lamda[0], alpha2 * lamda[1], alpha3 * lamda[2]))

        add_num = np.dot(p, v)

        img2 = np.array([img[:, :, 0] + add_num[0], img[:, :, 1] + add_num[1], img[:, :, 2] + add_num[2]])

        img2 = np.swapaxes(img2, 0, 2)
        img2 = np.swapaxes(img2, 0, 1)

        misc.imsave(save_dir_tt + np.str(name_num) + '.jpg', img2)
        name_num += 1
    return image_list

def pcaCreate_Ori(image_files,dir):
    parser = argparse.ArgumentParser()
    parser.add_argument("file_suffix", help="specific the file suffix")
    parser.add_argument("root_dir", help="E:\\")
    parser.add_argument("-f", "--file", help="record result to file")
    parser.add_argument("data_set",help= "specific the file suffix")
    args = parser.parse_args()
    img_num = len(os.listdir(args.root_dir + '/' + args.dataset))
    for i in range(img_num):
        img_name = os.listdir(args.root_dir + '/' + args.dataset)[i]
        img = Image.open(os.path.join(args.root_dir, args.dataset, img_name))

        img = np.asarray(img, dtype='float32')
        img = img / 255.
        img_size = img.size / 3
        img1 = img.reshape(img_size, 3)
        img1 = np.transpose(img1)
        img_cov = np.cov([img1[0], img1[1], img1[2]])
        lamda, p = np.linalg.eig(img_cov)

        p = np.transpose(p)

        alpha1 = random.normalvariate(0, 0.3)
        alpha2 = random.normalvariate(0, 0.3)
        alpha3 = random.normalvariate(0, 0.3)
        v = np.transpose((alpha1 * lamda[0], alpha2 * lamda[1], alpha3 * lamda[2]))

        add_num = np.dot(p, v)

        img2 = np.array([img[:, :, 0] + add_num[0], img[:, :, 1] + add_num[1], img[:, :, 2] + add_num[2]])

        img2 = np.swapaxes(img2, 0, 2)
        img2 = np.swapaxes(img2, 0, 1)

        misc.imsave('test2222.jpg', img2)

dir_list = "xxx"

for dir in os.listdir(dir_list):

    image_files = glob.glob(dir_list + dir + "\\*.jpg")

    if len(image_files) == 0:
        continue

    name_num = 0
    image_list = pcaCreate(image_files, dir, name_num, dir_list)