from flask import Blueprint, request, jsonify

branch_and_bound = Blueprint('branch_and_bound ', __name__,url_prefix='/branch_and_bound ')