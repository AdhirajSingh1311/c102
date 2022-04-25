from email.mime import image
from os import access
from tracemalloc import take_snapshot
import cv2
import dropbox
import time
import random

startTime=time.time()

def takeSnapshot():
    no=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        imagename='img'+str(no)+'.png'
        cv2.imwrite(imagename,frame)
        startTime=time.time
        result=False
    return imagename
    print ("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadFiles(imagename):
    accesToken="riFu6Ybhc9AAAAAAAAAAHWkfE9AiGyD6n4254tOxesw7ShRjGjFhrjhRVa3NX3mx"
    file=imagename
    file_from =file
    file_to="/test"+(imagename)
    dbx=dropbox.Dropbox(accesToken)
    with open (file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,more=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=takeSnapshot()
            uploadFiles(name)
main()
    


