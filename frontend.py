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
@app.route("/search/<topic>",methods=['GET'])
def search(topic):
    result=requests.get("http://192.168.56.101:5000/search/{}".format(topic))
    return (result.content)

@app.route("/updateCost",methods=['PUT'])
def updateCost():
    id=request.json['ID']
    idInt=int(id)
    cost=request.json['COST']
    costInt=int(cost)
    result=requests.put("http://192.168.56.101:5000/updateCost",data={'ID':idInt,'COST':costInt})
    return (result.content)

@app.route("/queryNumbers",methods=['PUT'])
def queryNumbers():
     id=request.json['ID']
     idInt=int(id)
     amount=request.json['AMOUNTS']
     amountInt=int(amount)
     result=requests.put("http://192.168.56.101:5000/queryNumbers",data={'ID':idInt,'AMOUNTS':amountInt})
     return (result.content)

@app.route("/IncreaseNumbers",methods=['PUT'])
def IncreaseNumbers():
     id=request.json['ID']
     idInt=int(id)
     amount=request.json['AMOUNTS']
     amountInt=int(amount)
     result=requests.put("http://192.168.56.101:5000/IncreaseNumbers",data={'ID':idInt,'AMOUNTS':amountInt})
     return (result.content)

@app.route("/purchase/<id>",methods=['GET'])
def purchase():
     id=request.json['ID']
     idInt=int(id)
     result=requests.get("http://192.168.56.102:5000/purchase/{}".format(idInt))
     return (result.content)