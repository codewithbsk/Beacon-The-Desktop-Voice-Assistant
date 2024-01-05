import os
import pyautogui
import datetime

def takeSS():
    img_captured=pyautogui.screenshot()
    a=os.getcwd()
    if not os.path.exists("Screenshots"):
        os.mkdir("Screenshots")
    os.chdir(a+'\Screenshots')
    ImageName='screenshot-'+str(datetime.datetime.now()).replace(':','-')+'.png'
    img_captured.save(ImageName)
    os.startfile(ImageName)
    os.chdir(a)

    