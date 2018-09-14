from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import pymysql
import os
import sys

def readpasswd():
    f = open("./pass.txt","r")
    passwd=f.readlines()
    f.close()
    return passwd


def sql_insert(name, date_limit, weight, company=None):
    passwd = readpasswd()
    conn = pymysql.connect(host='localhost',user=passwd[0][:-1],password=passwd[1][:-1],db='qr_data',charset='utf8')
    curs = conn.cursor()
    sql =  "insert into qr_data(Name, Date_limit,Weight,Company) values(%s,%s,%s,%s)"
    curs.execute(sql,(name,date_limit,weight,company))
    conn.commit()
    conn.close()

def qr_scanning(stream):
    
    qrData =set()

    print("[INFO] starting video stream...")

    #initialize the video stream and allow the camera sensor to warm up
    time.sleep(2.0)


    while True:
        frame = stream.read()
        frame = imutils.resize(frame,width=400)
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            (x,y,w,h) = barcode.rect
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type

            text = "{} ({})".format(barcodeData,barcodeType)
            cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
            qrData.add(barcodeData) # add qr_code data to set.


        cv2.imshow("Barcode Scanner",frame)
        key = cv2.waitKey(1) &0xFF
        if key == ord("q"):
            break

    listData = list(qrData) #change set data to list data
    tuples=[] # list data that will have tuples of qr_code data

    for lists in listData:
        try:
            tuples.append(eval(lists)) #making string to tuple
        except:
            print("wrong qr code data")

    #data inserting to database
    for i in range(len(tuples)):
        for j in range(len(tuples[i])):
            print(tuples[i][j])

        if len(tuples[i]) ==3:
            sql_insert(tuples[i][0],tuples[i][1],tuples[i][2])
        elif len(tuples[i]) ==4:
            sql_insert(tuples[i][0],tuples[i][1],tuples[i][2],tuples[i][3])

    print("[INFO] quiting...")
    print("\n[INFO] sql update finished [press 'Enter' to 'continue']...")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    stream = VideoStream(0).start()
    qr_scanning(stream)
    stream.stop()
