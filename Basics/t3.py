# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:48:45 2020

@author: Harish

gray image is a mat rix of 2 channels

color image is a matrix of 3 channels

(730, 807, 3) 

(730, 807, 0),(730, 807, 1),(730, 807, 2)  it has three channels

write code(wc) for getting (b,g,r) values  at pixel no (0,0) 

wc to print vales upto 10 pixels
  

"""

import cv2
image=cv2.imread('1.jpg')


#at pixel (0,0) get (b,g,r) values,image is matrix

(b,g,r)=image[0,0]

print("b:%d,g:%d,r:%d"%(b,g,r))

for i in range(100):
    (b,g,r)=image[i,i]
    print("b,g,r",b,g,r)

#o/p:-b:255,g:255,r:255
cv2.imshow('image',image)
cv2.waitKey(0)


'''
o/p:-

runfile('H:/pics1/t3.py', wdir='H:/pics1')
b:255,g:255,r:255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 255 255
b,g,r 255 254 254
b,g,r 255 254 254
b,g,r 255 255 255
b,g,r 253 253 253
b,g,r 253 255 255
b,g,r 252 254 254
b,g,r 233 235 235
b,g,r 114 153 175
b,g,r 36 67 90
b,g,r 5 25 50
b,g,r 10 20 44
b,g,r 9 14 39
b,g,r 15 21 44
b,g,r 10 21 43
b,g,r 3 16 38
b,g,r 1 9 26
b,g,r 3 11 28
b,g,r 4 12 29
b,g,r 1 8 23
b,g,r 0 5 20
b,g,r 1 7 20
b,g,r 2 8 21
b,g,r 0 5 18
b,g,r 2 4 22
b,g,r 3 5 23
b,g,r 3 5 23
b,g,r 3 6 21
b,g,r 3 6 21
b,g,r 2 5 19
b,g,r 0 3 17
b,g,r 0 2 16
b,g,r 3 4 24
b,g,r 3 7 31
b,g,r 0 7 36
b,g,r 1 12 44
'''