from flask import Blueprint, request, jsonify

simple_recursive = Blueprint('simple_recursive ', __name__,url_prefix='/simple_recursive ')