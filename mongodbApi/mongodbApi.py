import pymongo
import datetime

class mongodbApi:

    def findAll(self, mongodbConfigDict):

        mongodbConnectionUrl = mongodbConfigDict["protocol"] + "://" + mongodbConfigDict["server"] + ":" + str(mongodbConfigDict["port"]) + "/"

        mongoClient = pymongo.MongoClient(mongodbConnectionUrl)

        dbObject = mongoClient[mongodbConfigDict["database"]]

        dbCollection = dbObject[mongodbConfigDict["collection"]]

        for log in dbCollection.find():

            print("\n" + str(log))

    def insertLog(self, mongodbConfigDict, apiConfigDict, clipboardContent, creator):

        mongodbConnectionUrl = mongodbConfigDict["protocol"] + "://" + mongodbConfigDict["server"] + ":" + str(mongodbConfigDict["port"]) + "/"

        mongoClient = pymongo.MongoClient(mongodbConnectionUrl)

        dbObject = mongoClient[mongodbConfigDict["database"]]

        dbCollection = dbObject[mongodbConfigDict["collection"]]

        insertDict = {
            "clipboardContent": clipboardContent,
            "created": datetime.datetime.now(),
            "creator": creator          
        }

        insertId = dbCollection.insert_one(insertDict)

        # print(insertId.inserted_id)

        publisherUrl = apiConfigDict["protocol"] + "://" + apiConfigDict["server"] + ":" + str(apiConfigDict["port"]) + "/" + str(insertId.inserted_id)

        query = { "_id": insertId.inserted_id }
        updateValue = { "$set": { "publisherUrl": publisherUrl } }

        updateId = dbCollection.update_one(query, updateValue)

        # print(updateId.modified_count)

        # print("\n" + str(dbCollection.find_one(insertId.inserted_id)))

        return dbCollection.find_one(insertId.inserted_id)