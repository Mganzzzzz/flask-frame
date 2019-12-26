import config
from exception.auth_exception import AuthLoginFailed
from exception.exception_code import ErrorCode
from werkzeug.security import generate_password_hash, check_password_hash
from . import *
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serialier,
    SignatureExpired,
    BadSignature,
)


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(150))
    deleted = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(100))
    created_time = db.Column(db.Integer, default=0)

    chats = db.relationship('Chat', backref="user")

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.avatar = form.get('avatar', 'tanaka')
        self.created_time = timestamp()

    def save(self):
        self.password = self.gen_passwork_hash(self.password)
        super().save()

    def gen_passwork_hash(self, passwd):
        hash_passwd = generate_password_hash(passwd)
        return hash_passwd

    def varify_password(self, passwd):
        return check_password_hash(self.password, passwd)

    # 验证注册用户的合法性的
    def valid(self):
        valid_username = User.query.filter_by(username=self.username).first() == None
        valid_username_len = 2 <= len(self.username) <= 20
        valid_password_len = 3 <= len(self.password) <= 20
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        if not valid_username_len:
            message = '用户名长度必须大于等于 3, 小于等于 20'
            msgs.append(message)
        if not valid_password_len:
            message = '密码长度必须大于等于 3, 小于等于 20'
            msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs

    def validate_login(self, u):
        is_passwd_valid = self.varify_password(u.password)
        return u.username == self.username and is_passwd_valid

    def change_password(self, password):
        if 3 <= len(password) <= 20:
            self.password = password
            self.save()
            return True
        else:
            return False

    def change_avatar(self, avatar):
        if 2 <= len(avatar) <= 1000:
            self.avatar = avatar
            self.save()
            return True
        else:
            return False

    @staticmethod
    def gen_token(user_id, ):
        auth_s = Serialier(config.secret_key, config.expire_time)
        token = auth_s.dumps({"id": user_id})
        return token.decode('ascii')

    @staticmethod
    def auth_token(token):
        auth_s = Serialier(config.secret_key, config.expire_time)
        try:
            auth_s.loads(token)
        except SignatureExpired as e:
            raise AuthLoginFailed('token 超时 请重新登录', ErrorCode.TokenExprie)
        except BadSignature as e:
            raise AuthLoginFailed('token 错误', ErrorCode.TokenError)
