# -*- coding: utf-8 -*-
'''
정수 값을 입력받아 제곱하여 출력
Positional argument
'''
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("square",help="display a square of a given number", type=int)
args=parser.parse_args()
print(args.square**2)