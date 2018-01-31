import threading
from time import ctime,sleep
import serial
import qrcode
import time
import binascii

#serial init
ser=serial.Serial("/dev/ttyAMA0",9600)

test=hex(0x01)

threads=[]

global serialText
serialText=""
text=""
#if photograph error photograph time
photographTime=2
getQRcodeFlag=False

#use camera to get one .png and get it's qrcode
def getQrcodeResult():
    result=qrcode.lesen().strip() 
    result=result[9:]
    return result

def clearSerialBuffer():
    global serialText
    n=ser.inWaiting()
    serialText=str(binascii.b2a_hex(ser.read(n)))[0:]

while (True):
    if(ser.inWaiting()>0):   
        clearSerialBuffer()
        if(serialText=="01"):
            ser.write("\x01".encode('utf-8'))
        else:
            for i in range(0,photographTime):
                text=getQrcodeResult()
                if(text!=""):
                    ser.write(text)
                    getQRcodeFlag=True
                    break
            #fail to get QRcode serial send 0
            if(getQRcodeFlag==False):
                ser.write("0")
            getQRcodeFlag=False    
GPIO.cleanup()
ser.close()
