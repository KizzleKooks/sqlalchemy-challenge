from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def home():
 

