## this is the test code that is written on other website
## I brought this source code from https://www.learnopencv.com/barcode-and-qr-code-scanner-using-zbar-and-opencv/
#from PIL import Image
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(im):
    #find barcodes and QRcode
    decodedObjects=pyzbar.decode(im)

    #print results
    for obj in decodedObjects:
        print('Type : ',obj.type)
        print('Data : ',obj.data.decode('utf-8'),'\n')
    return decodedObjects

#display barcode and QR code location
def display(im, decodedObjects):
    for decodedObject in decodedObjects:
        points=decodedObject.polygon

        if len(points) >4:
            hull=cv2.convexHull(np.array([point for point in points],dtype=np.float32))
            hull=list(map(tuple,np.squeeze(hull)))
        else:
            hull=points

        n = len(hull)

        for j in range(0,n):
            cv2.line(im,hull[j],hull[(j+1)%n],(255,0,0),3)
    cv2.imshow("Results",im)
    cv2.waitKey(0)

def Main():
    im=cv2.imread('code.png')
    decodedObjects=decode(im)
    display(im,decodedObjects)

if __name__ == '__main__':
    Main()
