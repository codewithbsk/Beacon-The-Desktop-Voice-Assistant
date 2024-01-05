from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

root = Tk()
root.attributes('-topmost', True)
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

def play_gif():
    global img
    img = Image.open("Your address where you have saved the beacon.gif file \\Beacon.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)

while True:
    play_gif()
    time.sleep(5)
    root.mainloop()
