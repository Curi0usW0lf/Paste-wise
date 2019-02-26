import requests
import json


class messages:

    def __init__(self, teamsApiConfigDict, teamsApiEndpointsDict):

        self.teamsApiUrl = teamsApiConfigDict["teamsApiUrl"]
        self.teamsApiBearerToken = teamsApiConfigDict["teamsApiBearerToken"]
        self.teamsApiEndpoints = teamsApiEndpointsDict

        self.defaultHeaders = {}
        self.defaultHeaders.update({'Content-Type': 'application/json'})
        self.defaultHeaders.update(
            {'Authorization': 'Bearer {}'.format(self.teamsApiBearerToken)})

    def getHttpRequest(self, teamsApiEndpoint, roomId):

        # , auth=(self.apiUsername, self.apiPasskey)
        print("\n\tGet Messages API URL - " + self.teamsApiUrl +
              self.teamsApiEndpoints[teamsApiEndpoint])

        httpUrl = self.teamsApiUrl + self.teamsApiEndpoints[teamsApiEndpoint]

        payload = {
            "roomId": roomId,
            "max": 5
        }
        
        # , auth=(self.apiUsername, self.apiPasskey)
        r = requests.get(httpUrl, params=payload, headers=self.defaultHeaders)

        # print(r.request.url)
        # print(r.request.headers)
        # print(r.request.body)

        print("\n\tGet Messages API Status Code - " + str(r.status_code))

        # print("\n\tGet Messages API Response - " + str(r.text))

        if str(r.status_code) == 200:
            return {}

        return r.json()
