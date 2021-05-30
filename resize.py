import cv2
import numpy as np

def resize(img):
    dim = (626, 417)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return img