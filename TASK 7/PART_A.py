import cv2 as cv2
import numpy as np

image = cv2.imread('.\maze.jpg')


image2 = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

cv2.imshow('OG_img', image)
cv2.imshow('Filtered_img', image2)
cv2.waitKey(0)
