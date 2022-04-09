from flask import Flask, request, jsonify
import json
import requests
from time import sleep

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/info/<id>",methods=['GET'])
def info(id):
    idInt=int(id)
    result=requests.get("http://192.168.56.101:5000/info/{}".format(idInt), verify=False)
    return (result.content)

@app.route("/search/<topic>",methods=['GET'])
def search(topic):
    result=requests.get("http://192.168.56.101:5000/search/{}".format(topic))
    return (result.content)

@app.route("/updateCost/<id>",methods=['PUT'])
def updateCost(id):
    cost=request.json['COST']
    costInt=int(cost)
    result=requests.put("http://192.168.56.101:5000/updateCost/"+str(id),data={'COST':costInt})
    return (result.content)

@app.route("/queryNumbers/<id>",methods=['PUT'])
def queryNumbers(id):
     idInt=int(id)
     amount=request.json['AMOUNTS']
     amountInt=int(amount)
     result=requests.put("http://192.168.56.101:5000/queryNumbers/"+str(id),data={'AMOUNTS':amountInt})
     return (result.content)

@app.route("/IncreaseNumbers/<id>",methods=['PUT'])
def IncreaseNumbers(id):
     idInt=int(id)
     amount=request.json['AMOUNTS']
     amountInt=int(amount)
     result=requests.put("http://192.168.56.101:5000/IncreaseNumbers/"+str(id),data={'AMOUNTS':amountInt})
     return (result.content)

@app.route("/purchase/<id>",methods=['GET'])
def purchase(id):
     idInt=int(id)
     result=requests.get("http://192.168.56.102:6000/purchase/{}".format(idInt))
     return (result.content)