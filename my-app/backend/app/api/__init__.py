import redis
from flask import Flask
from flask_cors import CORS
from api.login import api_login
from api.logout import api_logout
from api.register import api_register
from datetime import timedelta
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'my_secret'
ACCESS_EXPIRES = timedelta(minutes=15)
REFRESH_EXPIRES = timedelta(days=30)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = ACCESS_EXPIRES
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = REFRESH_EXPIRES
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

CORS(app)

jwt = JWTManager(app)

revoked_store = redis.StrictRedis(host='localhost', port=6379, db=0,
                                  decode_responses=True)

@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token['jti']
    entry = revoked_store.get(jti)
    if entry is None:
        return True
    return entry == 'true'


app.register_blueprint(api_login)
app.register_blueprint(api_logout)
app.register_blueprint(api_register)

