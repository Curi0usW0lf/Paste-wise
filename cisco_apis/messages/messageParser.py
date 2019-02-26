class messageParser:

    def __init__(self, apiConfigDict):

        self.returnList = []
        self.apiConfigDict = apiConfigDict

        self.lastCopyThis = ""
        self.lastCopyThat = ""

    def checkKeywords(self, messagesDict):

        self.returnList = []

        # print(str(messagesDict))

        messagesList = list(messagesDict["items"])

        for message in messagesList:

            print("\nLast Copy That - " + str(self.lastCopyThat))
            print("Last Copy This - " + str(self.lastCopyThis))

            print("\n" + str(messagesList.index(message)) + " - " + str(message["text"]))

            # print(self.apiConfigDict["protocol"] + "://" + self.apiConfigDict["server"] + ":" + str(self.apiConfigDict["port"]) + "/")
            # print(str(message["text"]))

            print(str(self.apiConfigDict["protocol"] + "://" + self.apiConfigDict["server"] + ":" + str(self.apiConfigDict["port"]) + "/" not in str(message["text"])))

            if self.apiConfigDict["protocol"] + "://" + self.apiConfigDict["server"] + ":" + str(self.apiConfigDict["port"]) + "/" not in str(message["text"]):

                if message["text"] == ":copy-this":
                    
                    if messagesList.index(message) != 0:

                        # print(str((messagesList.index(message)))) # Handling Array starting with 0

                        # print(str(messagesList[messagesList.index(message)+1]))                                    

                        if str(messagesList[messagesList.index(message)-1]["text"]) != self.lastCopyThis:             

                            # if self.apiConfigDict["protocol"] + "://" + self.apiConfigDict["server"] + ":" + str(self.apiConfigDict["port"]) + "/" not in str(message["text"]):

                            #     print(str(message["text"]))

                            self.returnList.append(messagesList[messagesList.index(message)-1])
                            
                            self.lastCopyThis = messagesList[messagesList.index(message)-1]["text"]

                elif message["text"] == ":copy-that":
                    
                    if messagesList.index(message) != len(messagesList)-1:

                        if str(messagesList[messagesList.index(message)+1]["text"]) != self.lastCopyThat:         

                            # print(str((messagesList.index(message)))) # Handling Array starting with 0

                            # print(str(messagesList[messagesList.index(message)-1]))

                            # print(str(messagesList.index(message)))
                            # print(str(len(messagesList)-1))                    
                            
                            #     print(str(message["text"]))

                            self.returnList.append(messagesList[messagesList.index(message)+1])

                            self.lastCopyThat = messagesList[messagesList.index(message)+1]["text"]

        return self.returnList

