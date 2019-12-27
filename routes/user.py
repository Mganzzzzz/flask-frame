from filter.registration_form import LoginForm, RegisgerForm
from routes import *
from models.user import User
from utils.utils import log

main = Blueprint('user', __name__)

Model = User

@main.route('/profile')
@login_required
def profile():
    print('proifle')
    u = current_user()
    return responseJson(u)


@main.route('/update_password', methods=['POST'])
@login_required
def update_password():
    u = current_user()
    password = request.form.get('password', '')
    print('password', password)
    return responseJson(None)


@main.route('/update_avatar', methods=['POST'])
def update_avatar():
    u = current_user()
    avatar = request.form.get('avatar', '')


@main.route('/register', methods=['POST'])
def register():
    RegisgerForm(request.form)
    form = request.form
    u = User(form)
    u_valid = u.valid()
    print(u_valid)
    if u_valid[0]:
        u.save()
        print(u.id, u.username, u.password)
        token = User.gen_token(u.id)
        r = dict(token=token)
        return  responseJson(r)
    else:
        abort(410)


# 登录并获取token
@main.route('/login', methods=['POST', 'GET'])
def login():
    LoginForm(request.form)
    u = User(request.form)
    log('debug u', u)
    # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.validate_login(u):
        token = User.gen_token(user.id)
        r = dict(token = token)
        return responseJson(r)
    elif user is None:
        raise AuthLoginFailed(message='登录失败 用户名不存在')
    else:
        print('登录失败')
        raise AuthLoginFailed(message='登录失败 密码错误')


@main.route('/auth_token', methods=['POST'])
def valid_token():
    form = request.form
    token = form.get('token')
    r = User.auth_token(token)
    return responseJson(r)
