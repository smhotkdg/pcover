# -*- coding: utf-8 -*-
'''
argumentparsing ����
������ ���� if arg.Width...���� 0 or ������ ���������� true false����->"" (NULL, None) ����

'''
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--Width",help="Width value of Cover image", type=int)
parser.add_argument("--Height",help="Height value of Cover image", type=int)
args=parser.parse_args()

if args.Width!="":
	print('Width:',args.Width)
if args.Height!="":
	print('Height:',args.Height)
