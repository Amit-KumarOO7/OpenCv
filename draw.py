import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#rectangle
#cv.rectangle(blank, (0,0), (250,400),(255,0,255), thickness = -1)
#cv.imshow('Rectangle', blank)
#circle
#cv.circle(blank, (blank.shape[0]//2,blank.shape[1]//2), 50, (0,255,0), thickness = -1)
#cv.imshow('Circle', blank)
#line
#cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2) ,(255,255,255), thickness=1)
#cv.imshow('Line', blank)
#write text on a image
cv.putText(blank, 'Sup Bitch', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)
cv.imshow('Text', blank)

cv.waitKey(0); 