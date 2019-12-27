from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort
from flask import Response
from functools import wraps

from exception.auth_exception import AuthLoginFailed
from exception.not_found import NotFound
from models.user import User
from models.chat import Chat
import time
import json

from utils.utils import log


def check_token(token):
    return User.auth_token(token)


def not_authenticated():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def responseJson(d):
    res = dict(
        code=0,
        message='success',
        data=d,
    )
    print('debug res', res)
    return jsonify(res)


def current_user():
    header = request.headers
    token = header.get('auth')
    auth_info = User.auth_token(token)
    uid = auth_info.get('id', '')
    if uid is not None:
        u = User.query.get(uid)
        log('debug u', u.tojson())
        return u


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        header = request.headers
        token = header.get('auth')
        if not token:
            raise AuthLoginFailed('token is null')
        elif not check_token(token):
            raise AuthLoginFailed('')
        else:
            return f(*args, **kwargs)
    return function
