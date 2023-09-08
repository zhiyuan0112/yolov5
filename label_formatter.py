import xml.etree.ElementTree as ET
import os

classes = ['smoke']

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(in_path, in_fn, out_path):
    in_file = open(in_path + in_fn)  
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    if w == 0 or h == 0:
        return
    for obj in root.iter('object'):
        #difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes :
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file = open(out_path + '%s.txt'%in_fn[:-4], 'w')
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == '__main__':
    # process labels
    in_path = '/mnt/c/Work/RISC-V/code/pp_smoke/labels/main/'
    out_path = '/mnt/c/Work/RISC-V/code/pp_smoke/labels/train/'
    in_fns = os.listdir(in_path)
    for in_fn in in_fns:
        convert_annotation(in_path, in_fn, out_path)
