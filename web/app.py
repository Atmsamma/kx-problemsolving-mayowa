import os
from flask import Flask, Response, request, jsonify
from flask_pymongo import PyMongo
import docker
import json


app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/'+ os.environ['MONGODB_DATABASE']

mongo = PyMongo(app)
db = mongo.db

#default
@app.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )

#contianer health check
@app.route('/status', methods=['GET'])
def status():
    #### rember to point this only to the databases
    client = docker.from_env()
    
    health_list = []

    for c in client.containers.list(all=True):
        health_list.append({"id":c.short_id, "name":c.name, "image":c.image.tags[0] if len(c.image.tags)>0 else "unknown", 
                    "status":c.status
                    })

    return Response(json.dumps(health_list), mimetype="text/json")
    


# data endpoint
@app.route('/data', methods=['GET'])
def get_all_users():
    users = db.users

    data = []
    for q in users.find():
        
        data.append({'email' : q['email'], 'username' : q['username'], 
        'password' : q['password'],})

    return jsonify(
        status=True,
        data=data
    )

# Run the application
if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
