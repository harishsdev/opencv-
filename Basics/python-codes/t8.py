# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:06:56 2020

@author: Harish

wc for random circles

step1:-Declare the canvas

step2:- 
        use np.random.randinit for initialzing
        center of size=(2,)
        color of size=(3,)
        radius=single element
        
step3:-
         draw circles using cv2.circle using for loop
"""
import numpy as np
import cv2

canvas=np.zeros(shape=(1000,500,3),dtype='uint8')



for i in range(80):
    center=np.random.randint(0,255,size=(2,))
    radius=np.random.randint(100)
    color=np.random.randint(0,255,size=(3,)).tolist()
    cv2.circle(canvas, tuple(center), radius, color)
    cv2.imshow('canvas',canvas)
    cv2.waitKey(0)