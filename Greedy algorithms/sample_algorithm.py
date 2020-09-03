from flask import Blueprint, request, jsonify

greedy = Blueprint('greedy', __name__,url_prefix='/greedy')