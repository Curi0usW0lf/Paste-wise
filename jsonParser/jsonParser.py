import json

class jsonParser:

    def __init__(self):

        print("\n\tThis is the " + __name__ + " for Cisco DevNet Hackathon\n")

    def parseJson(self, rawData):

        return json.loads(rawData)        

        # print(type(rawData))
        # print(rawData[0]["username"])