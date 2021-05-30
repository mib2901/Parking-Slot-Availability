from main import *
import cv2
import numpy as np
import pandas as pd

values = pd.read_csv('stats.csv', header=0)
accuracy = 0


for i in range(7,12):
    empty = './parking-lot' + str(i) + '/parking-lot' + str(i) + '.jpg'
    greencount = values['Spaces'][i-7]
    img1 = cv2.imread(empty)

    link = './parking-lot' + str(i) + '/parking-lot' + str(i) + '_2' + '.jpg'
    img2 = cv2.imread(link)
    empty_prediction = prediction(greencount, img1, img2)
    #print(empty_prediction, values['2'][i-7])
    empty_prediction = abs(values['2'][i-7] - empty_prediction)
    empty_prediction = empty_prediction/values['2'][i-7]
    empty_prediction = empty_prediction*100
    empty_prediction = 100-empty_prediction
    accuracy += empty_prediction

    link = './parking-lot' + str(i) + '/parking-lot' + str(i) + '_3' + '.jpg'
    img2 = cv2.imread(link)
    empty_prediction = prediction(greencount, img1, img2)
    #print(empty_prediction, values['3'][i-7])
    empty_prediction = abs(values['3'][i-7] - empty_prediction)
    empty_prediction = empty_prediction/values['3'][i-7]
    empty_prediction = empty_prediction*100
    empty_prediction = 100-empty_prediction
    accuracy += empty_prediction

    link = './parking-lot' + str(i) + '/parking-lot' + str(i) + '_4' + '.jpg'
    img2 = cv2.imread(link)
    empty_prediction = prediction(greencount, img1, img2)
    #print(empty_prediction, values['4'][i-7])
    empty_prediction = abs(values['4'][i-7] - empty_prediction)
    empty_prediction = empty_prediction/values['4'][i-7]
    empty_prediction = empty_prediction*100
    empty_prediction = 100-empty_prediction
    accuracy += empty_prediction

    link = './parking-lot' + str(i) + '/parking-lot' + str(i) + '_5' + '.jpg'
    img2 = cv2.imread(link)
    empty_prediction = prediction(greencount, img1, img2)
    #print(empty_prediction, values['5'][i-7])
    empty_prediction = abs(values['5'][i-7] - empty_prediction)
    empty_prediction = empty_prediction/values['5'][i-7]
    empty_prediction = empty_prediction*100
    empty_prediction = 100-empty_prediction
    accuracy += empty_prediction

accuracy = accuracy//20
print('ACCURACY : ', end = ' ')
print(accuracy)