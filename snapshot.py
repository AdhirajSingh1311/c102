import cv2 
def takeSnapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("pic.jpg",frame)
        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
takeSnapshot()

