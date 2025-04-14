import os
import requests
import json
from flask import Flask, request, jsonify

server = Flask(__name__)

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "https://localhost:5173")
# AUTH_SERVICE_URL = 'https://localhost:5173'

@server.route('/login', methods=['POST'])
def root():
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@server.route('/login', methods=['GET','POST'])
def login():
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/login")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@server.route('/register', methods=['GET','POST'])
def register():
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/register")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))