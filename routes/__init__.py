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


def responseJson(d):
    res = dict(
        code=0,
        message='success',
        data=d,
    )
    print('debug res', res)
    return jsonify(res)


def current_user():
    uid = session.get('user_id')
    # token =
    # request.
    print('uid', uid)
    if uid is not None:
        u = User.query.get(uid)
        return u


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        u = current_user()

        print('login required', u)
        if u is None:
            print('not login')
            raise AuthLoginFailed()
        return f(*args, **kwargs)

    return function
