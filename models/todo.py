from models.user import User
from . import *


class Todo(db.Model, ModelMixin):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    user_id = db.Column(db.Integer)
    complete = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)
    created_time = db.Column(db.Integer, default=0)

    # chats = db.relationship('Chat', backref="user")

    def __init__(self, form):
        super(Todo, self).__init__()
        self.task = form.get('task', '')
        self.user_id = form.get('user_id', '')
        self.complete = False
        self.created_time = timestamp()

    # 验证添加todo合法性
    def valid(self):
        valid_user = User.query.filter_by(user_id=self.username).first() == None
        valid_task = 0 < len(self.task) <= 20
        msgs = []
        if not valid_user:
            message = '该用户不存在'
            msgs.append(message)
        if not valid_task:
            message = 'todo长度必须大于等于 3, 小于等于 20'
            msgs.append(message)
        status = valid_task and valid_user
        return status, msgs

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password

    def complete_password(self):
        self.complete = True
        self.save()
        return True

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
    def todos_by_userid(self, user_id):
        return Todo.query.filter_by(user_id=user_id)
