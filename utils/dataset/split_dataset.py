"""
Split train set into test and val
"""

import os
from os.path import join
import shutil

# move 100 pairs to test
train_path = 'data/dataset/smoke_1507/train'
train_fns_xml = sorted(os.listdir(join(train_path, 'Annotations')))
train_fns_img = sorted(os.listdir(join(train_path, 'images')))

i = 0
selected_nums = []
for (fn_xml, fn_img) in zip(train_fns_xml, train_fns_img):
    i += 1
    if i % 15 == 0:
        selected_nums.append(fn_xml[:-4])
        # switch
        # shutil.move(join(train_path, 'Annotations', fn_xml), 'data/dataset/smoke_1507/test/Annotations')
        # shutil.move(join(train_path, 'images', fn_img), 'data/dataset/smoke_1507/test/images')

print('Length of testing set:', len(selected_nums))
print(selected_nums)

# write the selected nums into txt
file_path = "data/dataset/smoke_1507/test.txt"
with open(file_path, "w") as file:
    for item in selected_nums:
        # file.write(f"{item}\n")
        pass


# move 100 pairs to test
train_path = 'data/dataset/smoke_1507/train'
train_fns_xml = sorted(os.listdir(join(train_path, 'Annotations')))
train_fns_img = sorted(os.listdir(join(train_path, 'images')))

i = 0
selected_nums = []
for (fn_xml, fn_img) in zip(train_fns_xml, train_fns_img):
    i += 1
    if i % 7 == 0:
        selected_nums.append(fn_xml[:-4])
        # switch
        # shutil.move(join(train_path, 'Annotations', fn_xml), 'data/dataset/smoke_1507/val/Annotations')
        # shutil.move(join(train_path, 'images', fn_img), 'data/dataset/smoke_1507/val/images')

print('Length of val set:', len(selected_nums))
print(selected_nums)

# write the selected nums into txt
file_path = "data/dataset/smoke_1507/val.txt"
with open(file_path, "w") as file:
    for item in selected_nums:
        # file.write(f"{item}\n")
        pass