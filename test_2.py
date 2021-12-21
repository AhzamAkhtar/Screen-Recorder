import cv2 as cv
import datetime
from win32api import GetSystemMetrics
width=GetSystemMetrics(0)
hight=GetSystemMetrics(1)
founrcc=cv.VideoWriter_fourcc("m","p","4","v")
time_stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename=f"{time_stamp}.mp4"
capture_video=cv.VideoWriter(filename,founrcc,20.0,(640,480))
capture=cv.VideoCapture(0)
while True:
    ret,frames=capture.read()
    cv.imshow("frame",frames)
    capture_video.write(frames)
    if cv.waitKey(10)==ord("q"):
        break
cv.destroyAllWindows()
capture.release()
capture_video.release()
