from PIL import Image
from xml.etree import ElementTree as ET
import os
import os.path
import time
#xml路径
path_xml='F:/wenjian4/all_kinds_pic/annotation'
files_xml=os.listdir(path_xml)
#图片路径
path_pic='F:/wenjian4/all_kinds_pic/pic'
files_pic=os.listdir(path_pic)

for file in files_xml:
    tree = ET.parse(path_xml+'\\'+file)
    root = tree.getroot()
    (path,tempfilename) = os.path.split(path_xml+'\\'+file)
    (filename,extension) = os.path.splitext(tempfilename)
    #读取xml对应图片
    for i in root.iter('filename'):
        img = Image.open(path_pic+filename+'.jpg') 
    j=0
    for i in root.iter('object'):       
        n=i.find('name')
        b=i.find('bndbox')
        Xmin=b.find('xmin')
        Ymin=b.find('ymin')
        Xmax=b.find('xmax')
        Ymax=b.find('ymax')
#判断文件夹存在及生成
        path_dir='F:/wenjian4/all_kinds_pic/drink/'+n.text
        isExists=os.path.exists(path_dir)
        if not isExists:
           os.makedirs(path_dir) 
        box=(int(Xmin.text),int(Ymin.text),int(Xmax.text),int(Ymax.text))
        img_cut = img.crop(box)
#防止一张图片中一种饮料有多瓶多加了个str(j)保证命名不重复
        img_cut.save(path_dir+'\\'+filename+'_'+n.text+'_'+str(j)+'.jpg','JPEG')
        j=j+1
        #time.sleep(1)
        print (filename)
        print (n.text,Xmin.text,Ymin.text,Xmax.text,Ymax.text)
print("all done!")
