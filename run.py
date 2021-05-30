from main import *
import cv2
import numpy as np

print('Enter the empty plot image : ')
link = input()
img1 = cv2.imread(link)

print('Enter the number of plots : ')
greencount = int(input())

print('Enter the new plot image : ')
link = input()
img2 = cv2.imread(link)

prediction(greencount, img1, img2)