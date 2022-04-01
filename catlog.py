from crypt import methods
from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/info/<id>",methods=['GET'])
def info(id):
    with open('/home/amnakhdair/Desktop/projects/BooksDB.json', 'r') as DBfile:
        data = DBfile.read()
        jsonObject = json.loads(data)
        BooksRecords = jsonObject['BOOK']
        idInt = int(id)
        result=[BooksRecordsItem for BooksRecordsItem in BooksRecords if BooksRecordsItem['ID'] == idInt]
        if len(result)==0:
            return  "No such Book Found!!"
        return jsonify([{"ID":result[0]['ID'],"Title":result[0]['NAME']}])

@app.route("/search/<topic>",methods=['GET'])
def search(topic):
    with open('/home/amnakhdair/Desktop/projects/BooksDB.json', 'r') as DBfile:
        data = DBfile.read()
        jsonObject = json.loads(data)
        BooksRecords = jsonObject['BOOK']
        result=[BooksRecordsItem for BooksRecordsItem in BooksRecords if BooksRecordsItem['TOPIC'] == topic]
        arr=[]
        i=0
        for x in result:
            arr.append({"ID":result[i]["ID"],"NAME":result[i]['NAME']})
            i=i+1
        if len(result)==0:
            return  "No Such Book That Have The Same Topic Found!!"
        return jsonify([arr])
