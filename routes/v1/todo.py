from exception.form_valid_fali import FormValidFail
from filter import RegistrationForm
from routes import *
from models.user import User
from models.todo import Todo
from utils.utils import log

main = Blueprint('todo', __name__)

Model = User


@main.route('/all', methods=['GET'])
@login_required
def todo_all():
    u = current_user()
    if u is not None:
        todos = Todo.todos_by_userid()
    else:
        pass
    return responseJson([])


@main.route('/add', methods=['POST'])
# @login_required
def todo_add(form):
    log('debug form')
    u = current_user()
    form = RegistrationForm(request.form)
    todo = Todo(form)
    chatValid = todo.valid()
    if chatValid:
        todo.save()
    else:
        return render_template('register.html')


@main.route('/delete')
def todo_delete():
    u = current_user()
    if u is not None:
        return render_template('profile.html', user=u)
    else:
        return redirect(url_for('.index'))


@main.route('/update', methods=['POST'])
def todo_update():
    u = current_user()
    password = request.form.get('password', '')
    print('password', password)
    if u.change_password(password):
        print('用户密码修改成功')
    else:
        print('用户密码修改失败')
    return redirect(url_for('user.profile'))


@main.route('/complete/<int:todo_id>')
@login_required
def todo_complete(todo_id):
    u = current_user()
    t = Todo.query.get(todo_id)
    if t is not None:
        if t.user_id is u.id:
            # t.comp
            pass
        else:
            pass
