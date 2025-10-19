from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# ---------- MongoDB Connection ----------
client = MongoClient("mongodb://localhost:27017/")
db = client["flask_db"]
collection = db["submissions"]

# ---------- Route 1: API Route ----------
@app.route('/api')
def get_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

# ---------- Route 2: Form Page ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']

            if not name or not email:
                return render_template('form.html', error="All fields are required")

            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for('success'))

        except Exception as e:
            return render_template('form.html', error=str(e))
    
    return render_template('form.html')

# ---------- Route 3: Success Page ----------
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
