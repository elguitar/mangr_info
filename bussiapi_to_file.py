#!/usr/bin/env python3

import urllib.request
import os
import sys

def getjson(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html.decode()

def readConfig(filename):
    optiondict = {}
    with open(filename, 'r') as configfile:
        for row in configfile:
            options = row.split(' = ')
            options[1] = options[1].replace("\n", "")
            optiondict[options[0]] = options[1]
    return optiondict

def main():
    stop = 3735
    linjojenmaara = 5
    options = readConfig(os.path.dirname(os.path.realpath(sys.argv[0])) + "/options/busapi.conf")
    url = "http://api.publictransport.tampere.fi/prod/?request=stop&user=" + options["user"] + "&pass=" + options["password"] + "&code=" + str(stop) + "&dep_limit=" + str(linjojenmaara)
    print(url)
    result = getjson(url)
    with open(os.path.dirname(os.path.realpath(sys.argv[0])) + '/db/bussit.json', 'w') as f:
        f.write(result)

main()
