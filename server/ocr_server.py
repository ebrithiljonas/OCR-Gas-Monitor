import cv2
import numpy as np
from PIL import Image
import pytesseract

def getText(img, crop):
    crop_img = img[crop[0]:crop[0]+crop[1], crop[2]:crop[2]+crop[3]]
    text = pytesseract.image_to_string(crop_img)
    return text;

filename = "/home/jonas/Downloads/a.png"
img = cv2.imread(filename)
c = [0, 400, 0, 500]
print(getText(img, c))