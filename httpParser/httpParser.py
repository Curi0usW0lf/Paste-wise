import urllib.parse
import requests
import json


class httpParser:

    # def __init__(self):

    #     self.apiUrl = "https://api.ciscospark.com"
    #     self.apiBearerToken = "NTM4MDhhMDEtYzU2Ni00NGQ0LTkyODQtNmExMTc4ZTVmZThjNGY2OTQ4ODEtYzg2_PF84_consumer"

    def __init__(self, apiConfigDict, endpointDict):

        self.apiUrl = apiConfigDict["apiUrl"]
        self.apiBearerToken = apiConfigDict["apiBearerToken"]
        self.apiEndpoints = endpointDict

        self.defaultHeaders = {}
        self.defaultHeaders.update({'Content-Type': 'application/json'})
        self.defaultHeaders.update(
            {'Authorization': 'Bearer {}'.format(self.apiBearerToken)})

    def getHttpRequest(self):

        # , auth=(self.apiUsername, self.apiPasskey)
        print("\n\tGet API URL - " + self.apiUrl + self.apiEndpoints["rooms"])

        httpUrl = self.apiUrl + self.apiEndpoints["rooms"]

        r = requests.get(httpUrl, headers=self.defaultHeaders)

        print("\n\tGet API Status Code - " + str(r.status_code))

        print("\n\tGet API Response - " + str(r.text))

    def postHttpRequest(self):

        print("\n\tAPI URL - " + self.apiUrl + self.apiEndpoints["messages"])

        httpUrl = self.apiUrl + self.apiEndpoints["messages"]

        payload = {
            "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjdlNWEwMzAtMzkzNi0xMWU5LWI3MGItMDdkODM3MzQzNTc0",
            "text": "."
        }
        # "toPersonId": "",
        #     "toPersonEmail": "",
        #     "text": "",
        # "files": ""

        # , auth=(self.apiUsername, self.apiPasskey)
        r = requests.post(httpUrl, data=json.dumps(payload), headers=self.defaultHeaders)

        print(r.request.url)
        print(r.request.headers)
        print(r.request.body)

        print("\n\tAPI Status Code - " + str(r.status_code))

        print("\n\tAPI Response - " + str(r.text))

    def putHttpRequest(self):

        print("\n\tAPI URL - " + self.apiUrl)

        payload = {'some': 'data'}
        headers = {'content-type': 'application/json'}

        # , auth=(self.apiUsername, self.apiPasskey)
        r = requests.post(self.apiUrl, data=json.dumps(
            payload), headers=headers)

        print("\n\tAPI Status Code - " + str(r.status_code))

    def deleteHttpRequest(self):

        print("\n\tAPI URL - " + self.apiUrl)

        payload = {'some': 'data'}
        headers = {'content-type': 'application/json'}

        # , auth=(self.apiUsername, self.apiPasskey)
        r = requests.post(self.apiUrl, data=json.dumps(
            payload), headers=headers)

        print("\n\tAPI Status Code - " + str(r.status_code))
