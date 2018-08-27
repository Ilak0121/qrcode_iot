import cv2 as cv

title="This is for test"
cv.NamedWindow(title,1)
capture=cv.CaptureFromCAM(0)

while(True):
    img = cv.QueryFrame(capture)
    cv.ShowImage(title,img)
