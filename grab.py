import win32gui
import win32ui 
import win32con
import numpy as np
from PIL import Image

import cv2

w = 640
h = 480

fourcc = cv2.cv.CV_FOURCC(*'VP80')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (w,h))



hwnd = 0 #win32gui.FindWindow(None, "Spotify")

wDC = win32gui.GetWindowDC(hwnd)
dcObj=win32ui.CreateDCFromHandle(wDC)
cDC=dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
cDC.SelectObject(dataBitMap)

for i in range(100):
	cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
	#dataBitMap.SaveBitmapFile(cDC, "imgs/grab_%d.png" % i)
	bmpstr = dataBitMap.GetBitmapBits(True)
	pil_img = Image.frombuffer( 'RGB',
            (w,h),
            bmpstr, 'raw', 'BGRX', 0, 1)

	array = np.array( pil_img )
	cvimage = cv2.cvtColor(array, cv2.COLOR_RGBA2BGRA)
	out.write(cvimage)

out.release()

# Free Resources
dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)
win32gui.DeleteObject(dataBitMap.GetHandle())