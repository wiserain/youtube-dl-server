import os
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

basic_auth = HTTPBasicAuth()

AUTH_DATA = {}

authuser = os.getenv('YTBDL_SERVER_USER', '')
authpass = os.getenv('YTBDL_SERVER_PASS', '')
if authuser and authpass:
    AUTH_DATA.update({authuser: generate_password_hash(authpass)})


@basic_auth.verify_password
def verify(username, password):
    if not bool(AUTH_DATA):
        return True
    if not (username and password):
        return False
    if username in AUTH_DATA and check_password_hash(AUTH_DATA.get(username), password):
        return username
