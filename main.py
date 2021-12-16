# pip install Pillow
# pip install numpy
# USING PYWIN32 TO GET THE HEIGHT AND WIDTH OF OUR WINDOW SCREEN
from PIL import ImageGrab
import numpy as np
import cv2 as cv
from win32api import GetSystemMetrics
import datetime
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
fourcc=cv.VideoWriter_fourcc("m","p","4","v")
time_stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_name=f"{time_stamp}.mp4"
capture_video=cv.VideoWriter(file_name,fourcc,20.0,(width,height))
webcam=cv.VideoCapture(0)
print(width,height)
while True:
    img=ImageGrab.grab(bbox=(0,0,width,height))
    # CONVERTING IT TO AN ARRAY SO THAT OPENCV CAN USE IT
    img_np=np.array(img)
    img_final=cv.cvtColor(img_np,cv.COLOR_BGR2RGB)
    ret,frame=webcam.read()
    fr_height,fr_width,_=frame.shape
    img_final[0:fr_height,0:fr_width,:]=frame[0:fr_height,0:fr_width,:]
    cv.imshow("capture",img_final)
    #cv.imshow("webcam",frame)
    capture_video.write(img_final)
    if cv.waitKey(10)==ord("q"):
        break
cv.destroyAllWindows()