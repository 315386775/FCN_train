# coding = utf-8  
# To prepare data may need the code.
# Change the image channels when you use the opencv.
import numpy as np
import cv2
def preprocess(image):
    """Takes an image and apply preprocess"""
    # 调整图片大小成网络的输入
    image = cv2.resize(image, (data_shape, data_shape))
    # 转换 BGR 到 RGB
    image = image[:, :, (2, 1, 0)]
    # 减mean之前先转成float
    image = image.astype(np.float32)
    # 减 mean
    image -= np.array([123, 117, 104])
    # 调成为 [batch-channel-height-width]
    image = np.transpose(image, (2, 0, 1))
    image = image[np.newaxis, :]
    # 转成 ndarray
    image = nd.array(image)
    return image

image = cv2.imread('img/xxx.jpg')
x = preprocess(image)
print('x', x.shape)