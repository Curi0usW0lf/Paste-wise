#!/usr/bin/env python3
from pathlib import Path
import json

# Import Classes
from jsonParser.jsonParser import jsonParser
from httpParser.httpParser import httpParser

# Read Config file, if exists
configDict = {}
configFile = Path("./config.json")

if configFile.is_file():
    f = open("config.json", "r+")
    configDict = json.loads(f.read())
    f.close()

# Class Initializaion
jsonParser = jsonParser()
if configDict:
    httpParser = httpParser(configDict["apiConfig"], configDict["apiEndpoints"])
else:
    httpParser = httpParser()

# Code Execution Starts
f = open("sample.json", "r+")
rawData = f.read()
f.close()

jsonParser.parseJson(rawData)

# httpParser.getHttpRequest()
httpParser.postHttpRequest()

# Code Execution Stops here
print("\n")
