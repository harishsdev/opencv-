# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:48:10 2020

step1:-Declare canvas shape

step2:-np.zeros for canvas formation

step3:-show canvas image 

step4:-(b,g,r),255 is highest value

declare red color tuple as (0,0,255) and green as 

blue=(255,0,0)
green=(0,255,0)
red=(0,0,255)

step5:-draw line on the canvas from pt1 to pt2

here in this example code overwritten of lines in canvas will occur

@author: Harish
"""

import cv2
import numpy as np

#canvas shape of 3 channels

canvas_shape=(500,500,3)

#blue color

blue=(255,0,0)

#declare the green color
green = (0, 255, 0)

#declare the red color
red=(0,0,255)



#declare the canvas using np.zeros

canvas=np.zeros(canvas_shape,dtype='uint8')
cv2.imshow('canvas',canvas)
cv2.waitKey(0)

#
pt1=(0,0)
pt2=(100,100)
color=red

cv2.line(canvas, pt1, pt2, color)
cv2.imshow('canvas',canvas)
cv2.waitKey(0)

#drawing red color with thickness of 60

cv2.line(canvas, pt1, pt2, color,thickness=60)
cv2.imshow('canvas',canvas)
cv2.waitKey(0)

#drawing green color on the canvas with thickness of 4
color=green

cv2.line(canvas, pt1, pt2, color,thickness=4)
cv2.imshow('canvas',canvas)
cv2.waitKey(0)


#drawing blue color on the canvas with thickness of 4

color=blue
cv2.line(canvas, pt1, pt2, color,thickness=1)
cv2.imshow('canvas',canvas)
cv2.waitKey(0)
