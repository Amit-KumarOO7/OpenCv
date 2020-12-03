import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\OpenCv\Basic\Resources\Photos\cat.jpg')
cv.imshow('Cat', img)

# plt.imshow(img)

# plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

rgb = cv.cvtColor(img, cv.COLOr_BGR2RGB)
cv.imshow('rgb, rgb')

cv.waitKey(0)