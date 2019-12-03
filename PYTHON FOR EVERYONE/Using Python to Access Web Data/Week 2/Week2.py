# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:25:50 2019

@author: Reda
"""

# Old School
import re

hand = open(r"D:\University of Michigan\PYTHON FOR EVERYONE\Using Python to Access Web Data\Chapter 11\regex_sum_263052.txt")
x = list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

res = 0
for z in x:
    res = res + int(z)

print(res)
print(x)
