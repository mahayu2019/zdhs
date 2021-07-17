#!/usr/bin/env python
# coding=utf-8

'''
文件自动分类
'''

import os
import shutil

src_folder = 'e:\\dl\\'  # 要整理的文件所在文件夹
des_folder = 'e:\\dls\\'  # 整理后存放的文件夹
files = os.listdir(src_folder)
print(files)  # 显示待整理的文件清单
for i in files:
    src_path = src_folder + i  # 原文件路径与文件名组合形成完整路径
    if os.path.isfile(src_path):  # 检查路径是否为文件
        des_path = des_folder + i.split('.')[-1]
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        shutil.move(src_path, des_path)
