from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token, get_jti,
    jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt)


api_logout = Blueprint('api_logout', __name__)

@api_logout.route("/logout", methods=['POST'])
@jwt_required
def logout():
    from api import revoked_store, ACCESS_EXPIRES
    jti = get_raw_jwt()['jti']
    revoked_store.set(jti, 'true', ACCESS_EXPIRES * 1.2)
    data = {"msg": "You're logged out"}
    return make_response(jsonify(data), 201)
