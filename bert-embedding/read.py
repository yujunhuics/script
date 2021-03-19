#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：NER 
@File    ：read.py
@Author  ：Junhui Yu
@Date    ：2021/1/22 19:55 
'''


import pickle



def padding_E2E_bert():
    # pad_embedding = pickle.load(open("pad_emb", "rb"))
    # print(type(pad_embedding[0]))
    #
    # train_embedding = pickle.load(open(r"D:\code\python\MGNER\THMG\data_emb\test.pkl", "rb"))
    # print(train_embedding)
    # train_embedding = pickle.load(open("test.pkl", "rb"))
    train_embedding = pickle.load(open("train_emb.pkl", "rb"))
    print(len(train_embedding))
    print(train_embedding[0][1][0].shape)

    print('-----------')
    print(train_embedding[0])
    # print(len(train_embedding[0][1]))
    # print(train_embedding[0][1][0])
    # print(len(train_embedding[1][0]))
    print(train_embedding[0][1].shape)
    print(train_embedding[0][1].shape)
    # print(train_embedding[10][1].shape)

padding_E2E_bert()
