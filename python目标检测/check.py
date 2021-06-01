from xml.etree import ElementTree as ET
import os
import os.path

path='C:\\Users\\Administrator\\Desktop\\annotations'
files=os.listdir(path)

for file in files:
    tree = ET.parse(path+'\\'+file)
    root = tree.getroot()
    (path,tempfilename) = os.path.split(path+'\\'+file)
    (filename,extension) = os.path.splitext(tempfilename)
    for i in root.iter('name'):
        if i.text not in ['canned drink','boxed drink','bottled drink']:
            print(filename)
