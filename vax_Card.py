# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:57:27 2021

@author: ABDUL REHMAN | +923325429252
"""
import os
import time
from cv2 import cv2
import random
import numpy as np
from PIL import Image
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from PIL import Image, ImageOps
from tkinter.filedialog import askopenfilenames

root = Tk()
root.geometry("200x70")


def Start():
    #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
   
    #BGfilename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
    BgImage = Image.open('bg.jpg')
    
    #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file

    #BgImage = Image.open(BGfilename[0])
    ImageBackground = BgImage.copy()
    
    img = cv2.imread(filename[0])
        #                      X
    front = img [135:950, 155:1455]
        #     TOP BAR             X
    back = img  [1020:1835 , 155:1455]
    
    cv2.imwrite("front.jpg", front)
    cv2.imwrite("back.jpg", back)
    front1 = Image.open('front.jpg')
    front1 = ImageOps.mirror(front1)
    front1 = front1.resize((822, 524))
    front1.save('front.jpg',format='JPEG', subsampling=0, quality=95)
    back1 = Image.open('back.jpg')
    back1 = ImageOps.mirror(back1)
    back1 = back1.resize((822, 524))
    back1.save('back.jpg', format='JPEG', subsampling=0, quality=95)
    Image0 = Image.open('front.jpg')
    Image1 = Image.open('back.jpg')
    
    # paste image giving dimensions
    
    ImageBackground.paste(Image0, (92, 63))
    ImageBackground.paste(Image1, (1004,63))
    
    ################################################
      # IMAGE 2
    img2 = cv2.imread(filename[1])
    front2 = img2 [135:950, 155:1455]
        #     TOP BAR             X
    back2 = img2  [1020:1835 , 155:1455]
    cv2.imwrite("front2.jpg", front2)
    cv2.imwrite("back2.jpg", back2)
    front22 = Image.open( 'front2.jpg')
    front22 = ImageOps.mirror(front22)
    front22 = front22.resize((822, 524))
    front22.save( 'front2.jpg', format='JPEG', subsampling=0, quality=95)
    back22 = Image.open('back2.jpg')
    back22 = ImageOps.mirror(back22)
    back22 = back22.resize((822, 524))
    back22.save('back2.jpg', format='JPEG', subsampling=0,quality=95)
    Image20 = Image.open( 'front2.jpg')
    Image21 = Image.open( 'back2.jpg')
    
    # paste image giving dimensions
    ImageBackground.paste(Image20, (92, 619))
    ImageBackground.paste(Image21, (1004, 619))
    
    ################################################
    # IMAGE 3
    img3 = cv2.imread(filename[2])
    front3 = img3 [135:950, 155:1455]
        #     TOP BAR             X
    back3 = img3  [1020:1835 , 155:1455]
    cv2.imwrite( "front3.jpg", front3)
    cv2.imwrite("back3.jpg", back3)
    front33 = Image.open('front3.jpg')
    front33 = ImageOps.mirror(front33)
    #front33 = front33.resize((816, 518))
    front33 = front33.resize((822, 524))
    front33.save('front3.jpg', format='JPEG', subsampling=0, quality=95)
    back33 = Image.open('back3.jpg')
    back33 = ImageOps.mirror(back33)
    #back33 = back33.resize((816, 518))
    back33 = back33.resize((822, 524))
    back33.save('back3.jpg', format='JPEG', subsampling=0, quality=95)
    Image30 = Image.open( 'front3.jpg')
    Image31 = Image.open('back3.jpg')
    # paste image giving dimensions
    
    ImageBackground.paste(Image30, (92, 1175)) #
    ImageBackground.paste(Image31, (1004, 1175))
    
    #############################################
    # IMAGE 4
    img4 = cv2.imread(filename[3])
    front4 = img4 [135:950, 155:1455]
        #     TOP BAR             X
    back4 = img4  [1020:1835 , 155:1455]
    cv2.imwrite("front4.jpg", front4)
    cv2.imwrite("back4.jpg", back4)
    front44 = Image.open( 'front4.jpg')
    front44 = ImageOps.mirror(front44)
    front44 = front44.resize((822, 524))
    front44.save('front4.jpg', format='JPEG', subsampling=0, quality=95)
    back44 = Image.open('back4.jpg')
    back44 = ImageOps.mirror(back44)
    back44 = back44.resize((822, 524))
    back44.save('back4.jpg', format='JPEG', subsampling=0, vquality=95)
    Image40 = Image.open('front4.jpg')
    Image41 = Image.open('back4.jpg')
      # paste image giving dimensions
      
    ImageBackground.paste(Image40, (92, 1731))
    ImageBackground.paste(Image41, (1004, 1731))
    
    #################################################    
      # IMAGE 5
    img5 = cv2.imread(filename[4])
    front5 = img5 [135:950, 155:1455]
        #     TOP BAR             X
    back5 = img5  [1020:1835 , 155:1455]
    cv2.imwrite("front5.jpg", front5)
    cv2.imwrite("back5.jpg", back5)
    front55 = Image.open('front5.jpg')
    front55 = ImageOps.mirror(front55)
    front55 = front55.resize((822, 524))
    front55.save('front5.jpg', format='JPEG', subsampling=0, quality=95)
    back55 = Image.open('back5.jpg')
    back55 = ImageOps.mirror(back55)
    back55 = back55.resize((822, 524))
    back55.save('back5.jpg', format='JPEG', subsampling=0, quality=95)
    Image50 = Image.open('front5.jpg')
    Image51 = Image.open('back5.jpg')
      # paste image giving dimensions
      
    ImageBackground.paste(Image50, (92, 2287))
    ImageBackground.paste(Image51, (1004, 2287))

# save images on desktop
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    ImageBackground.save(str(desktop) + '/print' + str(random.randrange(1001))+'.jpg', 'JPEG')
    
    print("Done")

# Function for closing window
def Close():
    root.destroy()

Start_Button = Button(root, text="Start", command=Start)
Start_Button.pack(pady=5)

exit_button = Button(root, text="Exit", command=Close)
exit_button.pack(pady=5)

root.mainloop()


