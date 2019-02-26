from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from pymongo import MongoClient
import os

app = Flask(__name__)

title = "Paste-Wise"
heading = "Paste-Wise Dashboard"

mongoClient = MongoClient("mongodb://10.4.64.209:27017")  # host uri
dbObject = mongoClient.webex_teams  # Select the database
dbCollection = dbObject.paste_log  # Select the collection name


def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')

@app.route("/")
def allLogs():    
    logItem = dbCollection.find()
    return render_template('index.html', mode="get", logs=logItem, t=title, h=heading)
    
@app.route("/<string:log_id>", methods=['GET'])
def getLog(log_id):    
    logItem = dbCollection.find({"_id": ObjectId(log_id) })    
    return render_template('index.html', mode="get", logs=logItem, t=title, h=heading)

@app.route("/<string:log_id>", methods=['DELETE'])
def deleteLog(log_id):    
    logItem = dbCollection.find_one_and_delete({"_id": ObjectId(log_id) })
    return render_template('index.html', mode="delete", logs=logItem, t=title, h=heading)

# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     tasks.remove(task[0])
#     return jsonify({'result': True})


if __name__ == "__main__":

    app.run(host= '0.0.0.0', port=3010)
