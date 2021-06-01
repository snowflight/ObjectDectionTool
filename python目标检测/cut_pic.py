from PIL import Image
import os
import os.path
import numpy as np
import time
#import cv2

rootdir = r'F:\wenjian4\cs_pic\JPEGImages'
for parent, dirnames, filenames in os.walk(rootdir):#through all pic
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)
   
        img = Image.open(currentPath)
        print (img.format, img.size, img.mode)
        time.sleep(1)
        #img.show()
        box1 = (17, 16, 158, 189)#set position
        image1 = img.crop(box1) #start to cut
        image1.save(r"F:\wenjian4\cs_pic\cs"+'\\'+filename) #save the pic
