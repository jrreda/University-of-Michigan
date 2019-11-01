# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:42:47 2019

@author: Reda
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

current_count = 0
url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))

def parse_html(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while current_count < count:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    current_count += 1
print('Last Url: ', url,'\n', 'Name =', name)
