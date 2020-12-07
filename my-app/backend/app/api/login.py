from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, get_jti,
    jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt)


api_login = Blueprint('api_login', __name__)

@api_login.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data['username']
    pw = data['password']
    if username == "jack" and pw == "pw":
        from api import revoked_store, ACCESS_EXPIRES
        access_token = create_access_token(identity=username)
        access_jti = get_jti(encoded_token=access_token)
        revoked_store.set(access_jti, 'false', ACCESS_EXPIRES * 1.2)
        res = {"token": access_token}
        return make_response(jsonify(res), 201)
    else:
        error = {"msg": "Wrong credentials"}
        return make_response(jsonify(error), 401)
