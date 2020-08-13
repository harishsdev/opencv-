# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:37:08 2020

@author: Harish
"""
import cv2

image=cv2.imread('1.jpg')

cv2.imshow("image",image)

print(image.shape)

print(image.shape[0],image.shape[1],image.shape[2])

#o/p:-(730, 807, 3),730 807 3

(height,width)=image.shape[:2]

print("height:%d,width:%d"%(height,width))

#o/p:-height:730,width:807

cv2.waitKey(0)

