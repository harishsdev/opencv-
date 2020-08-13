# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:47:04 2020

@author: Harish

wc for circle drawing,for circle we need centre of circle

cv2.circle(img, center, radius, color)

step1:-declare canvas

step2:-declare the center co-ordinates as tuple

step3:- declare the radius length

step4:-declare the color tuple

step5:-put all to gether into cv2.circle
"""

import numpy as np
import cv2

#step1:-declare canvas

canvas_shape=(500,500,3)
canvas1=np.zeros(canvas_shape,dtype='uint8')
cv2.imshow('canvas',canvas1)
cv2.waitKey(0)

#step2:-declare the center co-ordinates as tuple
center=(50,50)

#step3:- declare the radius length

radius=50


#step4:-declare the color tuple

color=(255,0,0)

#step5:-put all to gether into cv2.circle


cv2.circle(canvas1,center, radius, color)
cv2.imshow('canvas1',canvas1)
cv2.waitKey(0)




