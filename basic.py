import cv2 as cv

img = cv.imread('E:\OpenCv\Basic\Resources\Photos\lady.jpg')
cv.imshow('Cat', img)

#converting to grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#Blur 
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascate
cany = cv.Canny(blur, 125, 175)
cv.imshow('Edges', cany)

#Dilating image
dilated = cv.dilate(cany, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#erode
eroded = cv.erode(dilated, (7,7), iterations = 3)
cv.imshow('Eroded', eroded)

#ReSize
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA)
cv.imshow('Resized', resized)

#Cropping

croped = img[50:200, 200:400]
cv.imshow("Croped", croped)
cv.waitKey(0)