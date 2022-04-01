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
        return jsonify([{"Numbers OF books":result[0]['NUMBERS'],"Cost":result[0]['COST']}])