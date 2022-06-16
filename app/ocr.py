import pytesseract
import PIL.Image
import cv2
import os

myconfig = r"--psm 6 --oem 3"

def extract(image_file):
    text = pytesseract.image_to_string(PIL.Image.open(image_file), config = myconfig)
    
    return text

if __name__ == "__main__":
    # pwd = os.getcwd()
    # test_path = os.path.join(pwd,'test-img.jpeg')
    # print(extract(test_path))
    pass

