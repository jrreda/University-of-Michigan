# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:23:56 2019

@author: Reda
"""

import urllib
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

while True:
    address = input("Enter location: ")

    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false','address':address})

    print('Retrieving',url)

    data = urllib.request.urlopen(url).read().decode()
    print('\n','Retrived',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    place_id = js["results"][0]['place_id']
    print("Place id:",place_id)