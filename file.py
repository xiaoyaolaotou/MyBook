#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/29 0029 上午 10:50
__Author__ = '村长'

import os

dic = []
dir = {}
def file(rootdir):
    for root,dirs,files in os.walk(rootdir):
        # print(root)
        print(files)
        # for dir in root:
        #     print(dir)

file('app01')
# print(dir)