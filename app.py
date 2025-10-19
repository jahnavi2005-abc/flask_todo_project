from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    data = request.form
    db.items.insert_one({
        "itemName": data['itemName'],
        "itemDescription": data['itemDescription']
    })
    return jsonify({"message": "Item saved!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
