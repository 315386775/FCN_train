# coding = utf-8  
import Image  

def  convert(width,height):
    im = Image.open("C:\\workspace\\PythonLearn1\\test_1.jpg")
    (x, y)= im.size
    x_s = width
    y_s = y * x_s / x
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    out.save("C:\\workspace\\PythonLearn1\\test_1_out.jpg")
if __name__ == '__main__':
    convert(256,256)