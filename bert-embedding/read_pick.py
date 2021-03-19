#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：NER 
@File    ：read_pick.py
@Author  ：Junhui Yu
@Date    ：2021/1/22 16:56 
'''

import pickle

# rb 以二进制读取
data_input = open('train_emb.pkl','rb')
read_data = pickle.load(data_input)
print(read_data)
data_input.close()