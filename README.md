# FCN Dataset
The code includes all the file that you need in the training stage for FCN.

# FCN training Blog 
http://blog.csdn.net/u010402786/article/details/72883421

# How to use this code 
1. The first step
Use the labelme toolbox to label the images that you need.
Labelme : https://github.com/wkentaro/labelme

2. The second step
add_color to images 

3. The third step
post_process, convert png24 to png8

4. Data Augmentation
keras_dataAug: Use the kreas to augment the image. 
dataAugment: The origin method to augment the image.
Jitering: The method use in alexnet network.

