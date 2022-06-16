import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 6 --oem 3"

def extract(image_file):
    text = pytesseract.image_to_string(PIL.Image.open(image_file), config = myconfig)
    print(text)

extract("/home/royale/Documents/py/jupyter/OCR Project/IMG_0093.jpeg")

