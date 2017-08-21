# coding = utf-8  
import Image  

def  convert(width,height):
    im = Image.open("C:\\xxx\\test.jpg")
    out = im.resize((width, height),Image.ANTIALIAS)
    out.save("C:\\xxx\\test.jpg")
if __name__ == '__main__':
    convert(256,256)