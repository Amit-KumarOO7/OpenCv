import cv2 as cv
import numpy as np

img = cv.imread('E:\OpenCv\Basic\Resources\Photos\park.jpg')
cv.imshow('Park', img)

#Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average', average)

#gaussian 
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gauss', gauss)

#median
median = cv.medianBlur(img, 7)
cv.imshow('Medain', median)

#bilateral
bilateral = cv.bilateralFilter(img, 10, 35,25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)