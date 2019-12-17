# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:44:54 2019

@author: Reda
"""


import urllib.request as ur
import xml.etree.ElementTree as ET

url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'

xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')
tree = ET.fromstring(xml)
counts = tree.findall('.//count')

total_number = 0
res = 0
for count in counts:
    res += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', res)

    