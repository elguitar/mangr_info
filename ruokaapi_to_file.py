#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os
import sys
import urllib.request

def getjson(url):
	with urllib.request.urlopen(url) as response:
		html = response.read()
	return html.decode()

def fetchfood():
	day = str(datetime.now()).split(' ')[0]
	#print(day)
	#day = "2016-10-24"
	url = "https://api.ruoka.xyz/" + day
	result = getjson(url)
	#print(result['restaurants'][0]['menus'][0]['meals'][0]['contents'][0]['name'])
	restaurants = result['restaurants']
	#print("moi")
	#print(result)
	#print("heihei")
	return result

def main():
	day = str(datetime.now()).split(' ')[0]
	url = "https://api.ruoka.xyz/" + day
	result = getjson(url)
	#print("moi")
	#print(result.encode('utf-8'))
	with open(os.path.dirname(os.path.realpath(sys.argv[0])) + '/db/ruoat.json', 'w') as f:
		f.write(result)

main()
