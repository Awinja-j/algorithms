from flask import Blueprint, request, jsonify

brute_force = Blueprint('brute_force', __name__,url_prefix='/brute_force')