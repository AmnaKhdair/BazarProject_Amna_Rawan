from crypt import methods
from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "hello"

@app.route("/purchase/<id>",methods=['GET'])
def purchase(id):
    idInt = int(id)
    result=requests.put("http://192.168.56.101:5001/queryNumbers",{'ID':idInt,'AMOUNT':1})
    return result.content