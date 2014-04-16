#-*- coding: utf-8 -*-
'''
argumentparsing 예제
문제는 현재 if arg.Width...에서 0 or 나머지 정수값으로 true false결정->"" (NULL, None) 사용
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
