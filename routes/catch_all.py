import os
import requests
from flask import Blueprint, request, Response, jsonify

# Use the same auth-frontend service URL
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-frontend:5173")
if not AUTH_SERVICE_URL.startswith(('http://', 'https://')):
    AUTH_SERVICE_URL = "http://" + AUTH_SERVICE_URL

catch_all_bp = Blueprint('catch_all', __name__)

@catch_all_bp.route('/', defaults={'path': ''})
@catch_all_bp.route('/<path:path>')
def catch_all(path):
    try:
        proxied_url = f"{AUTH_SERVICE_URL}/{path}"
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
