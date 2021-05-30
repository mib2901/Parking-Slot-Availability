import cv2
import numpy as np

def contouring(img):
    ret, thresh = cv2.threshold(img, 10, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    result = []
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        if w*h > 300 and w*h < 1000 and w<100:
            result.append([[x,y,w,h]])

    return img, result