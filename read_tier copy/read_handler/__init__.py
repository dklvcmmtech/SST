from flask import Flask
import os
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    print('Hello World')
    return "Hello World!"


@app.route("/events",methods=['GET'])
def getEvents():
    print("GETEVENTS")
    #validate_Function()
    ret_obj = {'return':'GET'}
    return jsonify(ret_obj)


