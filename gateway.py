import os
import requests
import json
from flask import Flask, request, jsonify

server = Flask(__name__)

from routes.auth_back import authBack_bp
from routes.auth_front import authFront_bp
from routes.catch_all import catch_all_bp


server.register_blueprint(authBack_bp, url_prefix=[
                                            '/api/v1/token',
                                            '/api/v1/token/refresh', 
                                            '/api-auth',
                                            '/api/v1/user/register'])
server.register_blueprint(authFront_bp, url_prefix='')
server.register_blueprint(catch_all_bp, url_prefix='')

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))