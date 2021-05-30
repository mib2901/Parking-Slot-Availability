import cv2
import numpy as np
import sys

from edge import *
from resize import *
from contour import *
from save import *

def prediction(greencount, img1, img2):

    img1 = resize(img1)
    img2 = resize(img2)

    result = np.copy(img1)

    img_edge1 = edge(img1)
    img_edge1, rectangle = contouring(img_edge1)
    for r in rectangle:
        for x,y,w,h in r:
            result = cv2.rectangle(result, (x+5,y+5), (x+w-5,y+h-5), (0,255,0), -1)

    diff = cv2.absdiff(img1, img2)
    diff = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    diff, rectangle = contouring(diff)

    redcount = 0
    for r in rectangle:
        for x,y,w,h in r:
            result = cv2.rectangle(result, (x+5,y+5), (x+w-5,y+h-5), (0,0,255), -1)
            redcount += 1

    if redcount < greencount: 
        print('Parking is available', end = ' ')
        print(greencount-redcount, end = '/')
        print(greencount)
    else:
        print('Parking not available', end = ' ')
        print(greencount-redcount, end = '/')
        print(greencount)

    #cv2.imshow('result1', diff)
    #cv2.imshow('empty', img1)
    #cv2.imshow('plot', img2)
    #cv2.imshow('result2', result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    save(result)

    return greencount-redcount