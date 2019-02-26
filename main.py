#!/usr/bin/env python3
from pathlib import Path
import json

# Import Classes
from jsonParser.jsonParser import jsonParser
from httpParser.httpParser import httpParser
from mongodbApi.mongodbApi import mongodbApi

# Read Config file, if exists
configDict = {}
configFile = Path("./config.json")

if configFile.is_file():
    f = open("config.json", "r+")
    configDict = json.loads(f.read())
    f.close()

# Class Initialization
jsonParser = jsonParser()
if configDict:
    httpParser = httpParser(configDict["teamsApiConfig"], configDict["teamsApiEndpoints"])
else:
    httpParser = httpParser()
mongodbApi = mongodbApi()

# Code Execution Starts
f = open("sample.json", "r+")
rawData = f.read()
f.close()

jsonParser.parseJson(rawData)

# httpParser.getHttpRequest("messages")
httpParser.postHttpRequest("messages")

# mongodbApi.findAll(configDict["dbConfig"])
# mongodbApi.insertLog(configDict["dbConfig"], configDict["apiConfig"], "Test Message 2", "Get Username Info from WebEx Teams")

# Code Execution Stops here
print("\n")
