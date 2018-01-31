import os, signal, subprocess

strfile1 = "qrcode"

def erzeugen():
    text=raw_input(u"enter text QRCode: ")
    os.system("qrencode -o"+strfile1+".png '"+text+"'")
#    print u"QRCode in: "+strfile1+".png"
    
def lesen():
    os.system("raspistill -t 10 -w 800 -h 600 -o /home/pi/cameraqr/image.png")
#    print u"raspistill finished"
    #zbarcam=subprocess.Popen("zbarcam --raw --nodisplay /dev/video0", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    #print u"zbarcam started successfully..."
    #qrcodetext=zbarcam.stdout.readline()
    zbarcam=subprocess.Popen("zbarimg --raw /home/pi/cameraqr/image.png", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    qrcodetext=zbarcam.stdout.readline()
 #   if qrcodetext!="":
 #       print qrcodetext
 #   else:
 #       print u"qrcodetext is empty"
        
    os.killpg(zbarcam.pid, signal.SIGTERM)
 #   print u"zbarcam stopped successfully..."
    return u"QRCode:  "+qrcodetext
