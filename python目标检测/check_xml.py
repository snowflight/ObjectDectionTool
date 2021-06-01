from xml.etree import ElementTree as ET
import os
import os.path
import time
from PIL import Image

path='F:\\wenjian4\\third_unite\\annotation_cs'
rootdir = r'F:\wenjian4\third_unite\pic_cs'
files=os.listdir(path)

for file in files:
    tree = ET.parse(path+'\\'+file)
    root = tree.getroot()
    (path,tempfilename) = os.path.split(path+'\\'+file)
    (filename,extension) = os.path.splitext(tempfilename)
    for i in root.iter('object'):
        n=i.find('name')
        b=i.find('bndbox')
        Xmin=b.find('xmin')
        Ymin=b.find('ymin')
        Xmax=b.find('xmax')
        Ymax=b.find('ymax')
        print (n.text,Xmin.text,Ymin.text,Xmax.text,Ymax.text)
        time.sleep(1)
        filename=(filename+'.jpg')
        currentPath = os.path.join(rootdir, filename)
        img = Image.open(currentPath)
        box1 = (Xmin, Ymin, Xmax, Ymax)#set position
        image1 = img.crop(box1) #start to cut
        image1.save(r"F:\wenjian4\cs_pic\cs"+'\\'+filename) #save the pic
    print(filename)
	
