import cv2 as cv
# capture = cv.VideoCapture('E:\OpenCv\Basic\Resources\Videos\dog.mp4')
# while True:
#    isTrue, frame = capture.read()
#    cv.imshow('Video', frame)

#    if cv.waitKey(20) & 0xFF == ord('d'):
#        break

# capture.release()
# cv.destroyAllWindows()


capture = cv.VideoCapture('E:\OpenCv\Basic\Resources\Videos\dog.mp4')


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


while True:
    isTrue, frame = capture.read()
    resizedFrame = rescaleFrame(frame, scale=0.3)

    cv.imshow('Normal', frame)
    cv.imshow('Resized', resizedFrame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllW indows()
