from flask import Blueprint, request, make_response, jsonify
from services.user_service import add_new_user

api_register = Blueprint('api_register', __name__)


@api_register.route("/register", methods=['POST'])
def register():
    data = request.json
    try:
        username = data['username']
        pw = data['password']
        new_user = add_new_user(username, pw)
        new_user.add()
        res = {"msg": "Add new user"}
        return make_response(jsonify(res), 201)
    except Exception as e:
        res = {"error": e}
        return make_response(jsonify(res), 401)
