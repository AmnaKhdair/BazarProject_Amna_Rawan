from crypt import methods
from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/info/<id>",methods['GET'])
def Info():
    
    return "hello world"