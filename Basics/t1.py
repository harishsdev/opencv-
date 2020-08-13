#execution
#H:\pics1> python .\t1.py --image .\1.jpg

#import libraries
import cv2
import argparse

#create arg parser

ap=argparse.ArgumentParser()

#add arg parser
ap.add_argument("-i","--image",required=True)

args=vars(ap.parse_args())

#read image
image=cv2.imread(args["image"])
#print height and width
print("height:%d"%(image.shape[0]))
print("width:%d"%(image.shape[1]))

#show image
cv2.imshow("image",image)
cv2.waitKey(0)