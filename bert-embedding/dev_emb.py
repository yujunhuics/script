#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：NER 
@File    ：test_emb.py
@Author  ：Junhui Yu
@Date    ：2021/1/22 16:29
'''


import ast
import pickle
import json

from bert_serving.client import BertClient
bc = BertClient(port=86500, port_out=86501, show_server_config=True, timeout=10000)
# vec = bc.encode(['First do it'])
# print('--------------------------------')
# print(vec.shape)



f=open(r'C:\Users\junhuy\Desktop\ACEEN-GENIA\622data_en\Dev_json','r',encoding='utf-8')

embedding_out=open('dev_emb10.pkl','wb')

# f_sentence=open("sentence.txt",'w',encoding='utf-8')
datas=f.readlines()

# for line in datas:
#     content=json.loads(line)["sentence"].split(' ')
#     print(content)
#     vec=bc.encode(content)
large_arr=[]
for line in datas[:5000]:
    arr=[]
    # sentence='First do it'.split(' ')
    sentence=json.loads(line)["sentence"].split(' ')
    print(sentence)
    vec = bc.encode(sentence)
    print(vec.shape)
    arr.append(sentence)
    arr.append(vec)
    # print(arr)
    large_arr.append(arr)


pickle.dump(large_arr,embedding_out,True)


embedding_out.close()
#
# print("----------------------")
# # rb 以二进制读取
# data_input = open('train_emb.pkl','rb')
# read_data = pickle.load(data_input)
# print(read_data)
# data_input.close()