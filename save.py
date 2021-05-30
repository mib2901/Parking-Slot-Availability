import numpy as np
import cv2

def save(img):
    dim = (626, 417) # dim[0] is width n dim[1] is height... just change these accordingly
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite('output.png', img)
    return