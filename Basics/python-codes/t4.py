# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:19:45 2020

@author: Harish

Drawing:-

line api cv2.line

canvas is a simple image

line will have a start and end point (x1,y1)  and (x2,y2)

cv2.line(canvas_name,starting_point,ending point,color)

"""
import cv2
import numpy as np

image=(200,200,3)

canvas=np.zeros(image,dtype='uint8')
cv2.imshow('canvas',canvas)
cv2.waitKey(0)

green=(0,255,0)
pt1=(0,0)
pt2=(100,100)
cv2.line(canvas,pt1,pt2,green)
cv2.imshow('canvas',canvas)
cv2.waitKey(0)

#

