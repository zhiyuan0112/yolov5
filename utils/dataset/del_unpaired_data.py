"""
Usage: delete the unlabelled data
"""

import os
from os.path import join
import shutil


src_path_xml = 'data/dataset/smoke_1597/Annotations'
src_path_img = 'data/dataset/smoke_1597/JPEGImages'

fns_xml = os.listdir(src_path_xml)
fns_img = os.listdir(src_path_img)

xmls, imgs = [], []
for fn in fns_img:
    imgs.append(fn[:-4])
for fn in fns_xml:
    xmls.append(fn[:-4])

print('The lengths of the original xml and img are:', len(xmls), len(imgs))

intersection_set = set(xmls) & set(imgs)
intersection_list = list(intersection_set)
print('The length of paired data:', len(intersection_list))
# print(intersection_list)

cnt = 0
for fn in fns_xml:
    if fn[:-4] not in intersection_list:
        cnt += 1
        continue
    shutil.copy(join(src_path_xml, fn), 'data/dataset/smoke_1507/train/Annotations')
print('xml del:', cnt)

cnt = 0
for fn in fns_img:
    if fn[:-4] not in intersection_list:
        cnt += 1
        continue
    shutil.copy(join(src_path_img, fn), 'data/dataset/smoke_1507/train/images')
print('img del:', cnt)
