from flask import Flask, request, jsonify
import json
import requests


app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/info/<id>",methods=['GET'])
def info(id):
    idInt=int(id)
    result=requests.get("http://192.168.56.101:5000/info/{}".format(idInt))
    return (result.content)
