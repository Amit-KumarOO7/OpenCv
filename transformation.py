import cv2 as cv
import numpy as np

img = cv.imread('E:\OpenCv\Basic\Resources\Photos\cat.jpg')
cv.imshow('Cat', img)

#translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x  left
# +x  right
# -y  up
# +y down


translated = translate(img, -100, -100)
cv.imshow('Translated', translated)

#rotaton

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45) # - to counter clockwise
cv.imshow('Rotated', rotated)

#resizing

resized = cv.resize(img,(5000,500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

#fliping

flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)