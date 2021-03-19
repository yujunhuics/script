#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：NER 
@File    ：server.py
@Author  ：Junhui Yu
@Date    ：2021/1/22 14:52 
'''
from bert_serving.server import BertServer
import argparse
parser = argparse.ArgumentParser()
# args = parser.parse_args(['-model_dir', 'F:\share\dataset\chinese_L-12_H-768_A-12',
args = parser.parse_args(['-model_dir', r'C:\Users\junhuy\Desktop\uncased_L-12_H-768_A-12',
                                     '-port', '86500',
                                     '-port_out', '86501',
                                     '-max_seq_len', 'NONE',
                                     '-mask_cls_sep',
                                     '-num_worker', '1',
                                     '-cpu'])
server = BertServer(args)
server.start()