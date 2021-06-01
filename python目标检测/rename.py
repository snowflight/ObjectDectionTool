from xml.etree import ElementTree as ET
import os
import os.path

path='F:\\wenjian4\\all_kinds_pic\\annotations'
files=os.listdir(path)

for file in files:
    tree = ET.parse(path+'\\'+file)
    root = tree.getroot()
    (path,tempfilename) = os.path.split(path+'\\'+file)
    (filename,extension) = os.path.splitext(tempfilename)
    for i in root.iter('name'):
        if i.text in ['xb','kkkl','jdb','bskl','src','sm','mndp','mndy','mndr','mndw','xcd','glc','btxl','t','xmtx']:
			#,'ksf','cy','bl','nfsq','hdbq','yb']:
            i.text='bottled drink'
        if i.text in ['hwlj','hbhc','hmlmc','hxcd']:
            i.text='boxed drink'
        if i.text in ['tkkkl','ht','tmndo','tmndg','twlj','tzb','tfdot','tfdos','tfdrt','tfdrs','tfdg','thqz']:
			#,'txb','hn','tbskl','tbskl']:
            i.text='canned drink'
    tree.write(filename + '.xml')
    print（filename）
print("all done!")

