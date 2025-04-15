import os
import requests
from flask import Blueprint, jsonify

AUTH_BACKEND_SERVICE_URL = os.getenv("AUTH_BACKEND_SERVICE_URL")
if not AUTH_BACKEND_SERVICE_URL.startswith(('http://', 'https://')):
    AUTH_BACKEND_SERVICE_URL = "http://" + AUTH_BACKEND_SERVICE_URL
    
authBack_bp = Blueprint('authBack', __name__)

@authBack_bp.route('/api/v1/user/register', methods=['register'])
def register():
    try:
        response = requests.post(f"{AUTH_BACKEND_SERVICE_URL}/api/v1/user/register")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@authBack_bp.route('/api/v1/token', methods=['login'])
def login():
    try:
        response = requests.post(f"{AUTH_BACKEND_SERVICE_URL}/api/v1/token")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
@authBack_bp.route('/api/v1/token/refresh', methods=['refresh_token'])
def refresh_token():
    try:
        response = requests.post(f"{AUTH_BACKEND_SERVICE_URL})/api/v1/token/refresh")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@authBack_bp.route('/api-auth/', methods=['GET'])
def api_auth():
    try:
        response = requests.get(f"{AUTH_BACKEND_SERVICE_URL}/api-auth/")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500