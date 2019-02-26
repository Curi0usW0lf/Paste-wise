import requests

class messages:

    def __init__(self, teamsApiConfigDict, teamsApiEndpointsDict):

        self.teamsApiUrl = teamsApiConfigDict["teamsApiUrl"]
        self.teamsApiBearerToken = teamsApiConfigDict["teamsApiBearerToken"]
        self.teamsApiEndpoints = teamsApiEndpointsDict

        self.defaultHeaders = {}
        self.defaultHeaders.update({'Content-Type': 'application/json'})
        self.defaultHeaders.update({'Authorization': 'Bearer {}'.format(self.teamsApiBearerToken)})

    def getHttpRequest(self, teamsApiEndpoint, roomId):

        # , auth=(self.apiUsername, self.apiPasskey)
        print("\n\tGet API URL - " + self.teamsApiUrl + self.teamsApiEndpoints[teamsApiEndpoint])

        httpUrl = self.teamsApiUrl + self.teamsApiEndpoints[teamsApiEndpoint]

        r = requests.get(httpUrl, headers=self.defaultHeaders)

        print("\n\tGet API Status Code - " + str(r.status_code))

        print("\n\tGet API Response - " + str(r.text))    