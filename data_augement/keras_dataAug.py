# -- coding utf-8 --
# Use the keras to augment the image.
__author__ = 'Yawei Li'

# import packages
import os
import glob
from scipy import misc
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
      rotation_range=180,
      height_shift_range=0.1,
      shear_range=0.2,
      zoom_range=0.1,
      horizontal_flip=True,
      vertical_flip=True,
      fill_mode='nearest')


def data_augmentation(image_files, dir):
    image_list = []
    new_file_name = dir
    save_dir = "xxx" + new_file_name

    for image_file in image_files:
        image_list.append(misc.imread(image_file))

    for image in image_list:
        x = img_to_array(image)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir=save_dir,
                                  save_prefix=dir, save_format='jpg'):
            i += 1
            if i > 99:
                break
    return image_list

# List all the files
dir_list = os.listdir("xxx")

for dir in dir_list:

    image_files = glob.glob("xxx" + dir + "/*.jpg")

    if len(image_files) == 0:
        continue

    image_list = data_augmentation(image_files, dir)


