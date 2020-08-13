# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:22:10 2020

@author: Harish

Aim to draw the create canvas and create rectangle

step1:-create canvas and color tuples

blue=(255,0,0)
green=(0,255,0)
red=(0,0,255)

step2:-create pt1 and pt2 co-ordinates tuples

step3:-use cv2.rectangle api to draw rectangle


"""

import cv2
import numpy as np

canvas1=np.zeros((500,500,3),dtype='uint8')
canvas2=np.zeros((500,500,3),dtype='uint8')
canvas3=np.zeros((500,500,3),dtype='uint8')

pt1=(0,0)
pt2=(100,100)
blue=(255,0,0)
color=blue

cv2.rectangle(canvas1, pt1, pt2, color)
cv2.imshow('canvas',canvas1)
cv2.waitKey(0)

pt1=(50,50)
pt2=(400,400)
blue=(255,0,0)
color=blue
cv2.rectangle(canvas2, pt1, pt2, color)
cv2.imshow('canvas',canvas2)
cv2.waitKey(0)

pt1=(10,10)
pt2=(300,300)
green=(0,255,0)
cv2.rectangle(canvas3, pt1, pt2, color=green,thickness=5)
cv2.imshow('canvas3',canvas3)
cv2.waitKey(0)



