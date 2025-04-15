import os
import requests
from flask import Blueprint, jsonify, request, Response

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL")
if not AUTH_SERVICE_URL.startswith(('http://', 'https://')):
    AUTH_SERVICE_URL = "http://" + AUTH_SERVICE_URL

authFront_bp = Blueprint('authFront', __name__)
    
@authFront_bp.route('/login', methods=['GET','POST'])
def login():
    try:
        # response = requests.get(f"{AUTH_SERVICE_URL}/login")
        # return response.content, response.status_code
        proxied_url = f"{AUTH_SERVICE_URL}/login"
        # Forward the method, headers, query parameters, and body if needed
        proxied_response = requests.request(
            method=request.method,
            url=proxied_url,
            headers={key: value for key, value in request.headers if key.lower() != 'host'},
            params=request.args,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        # Exclude certain headers that should be managed by Flask
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = {
            name: value for name, value in proxied_response.headers.items()
            if name.lower() not in excluded_headers
        }
        response = Response(proxied_response.content, proxied_response.status_code, headers)
        return response
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@authFront_bp.route('/register', methods=['GET','POST'])
def register():
    try:
        # response = requests.get(f"{AUTH_SERVICE_URL}/register")
        # return response.content, response.status_code
        proxied_url = f"{AUTH_SERVICE_URL}/register"
        # Forward the method, headers, query parameters, and body if needed
        proxied_response = requests.request(
            method=request.method,
            url=proxied_url,
            headers={key: value for key, value in request.headers if key.lower() != 'host'},
            params=request.args,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        # Exclude certain headers that should be managed by Flask
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = {
            name: value for name, value in proxied_response.headers.items()
            if name.lower() not in excluded_headers
        }
        response = Response(proxied_response.content, proxied_response.status_code, headers)
        return response
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500