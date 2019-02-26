#!/usr/bin/env python3
from pathlib import Path
import json
import time

# Import Classes
from jsonParser.jsonParser import jsonParser
from httpParser.httpParser import httpParser
from mongodbApi.mongodbApi import mongodbApi

from cisco_apis.messages.messages import messages
from cisco_apis.messages.messageParser import messageParser
# from cisco_apis.profile.profile import profile

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
    messages = messages(configDict["teamsApiConfig"], configDict["teamsApiEndpoints"])
else:
    httpParser = httpParser()
mongodbApi = mongodbApi()

messageParser = messageParser(configDict["apiConfig"])

# Code Execution Starts
# f = open("sample.json", "r+")
# rawData = f.read()
# f.close()

# jsonParser.parseJson(rawData)

# httpParser.getHttpRequest("messages")
# httpParser.postHttpRequest("messages", "Y2lzY29zcGFyazovL3VzL1JPT00vNjdlNWEwMzAtMzkzNi0xMWU5LWI3MGItMDdkODM3MzQzNTc0", "DummyText")

while (1):

    for roomId in configDict["stickySpaces"]:

        log2DbList = []

        # print(str(roomId))

        messagesDict = messages.getHttpRequest("messages", roomId)

        print(str(messagesDict))

        if messagesDict:

            log2DbList = messageParser.checkKeywords(messagesDict)

            print("\nlog2DbList - " + str(log2DbList))
            print(str(len(log2DbList)))

        if len(log2DbList) > 0:

            for log2DbItem in log2DbList:

                dbRecordFromDb = mongodbApi.insertLog(configDict["dbConfig"], configDict["apiConfig"],log2DbItem["text"], log2DbItem["personEmail"])

                httpParser.postHttpRequest("messages", roomId, str(dbRecordFromDb["publisherUrl"])) # Room ID - Y2lzY29zcGFyazovL3VzL1JPT00vNjdlNWEwMzAtMzkzNi0xMWU5LWI3MGItMDdkODM3MzQzNTc0

    time.sleep(configDict["scanTimeInterval"])

# mongodbApi.findAll(configDict["dbConfig"])
# mongodbApi.insertLog(configDict["dbConfig"], configDict["apiConfig"], "Test Message 2", "Get Username Info from WebEx Teams")

# Code Execution Stops here
print("\n")

