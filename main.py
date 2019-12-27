from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from werkzeug.exceptions import HTTPException
from exception import RestException
from exception.server_exception import ServerException
from models import db

from routes.index import main as routes_index
from routes.user import main as routes_user
from routes.v1.todo import main as routes_todo
from utils.utils import log

app = Flask(__name__)
db_path = 'chat.sqlite'
manager = Manager(app)


@app.errorhandler(Exception)
def allException(e):
    try:
        err = ServerException()  # default error
        if isinstance(e, RestException):  # restfule error
            err = e
        elif isinstance(e, HTTPException):  # http error

            exception_name = e.__class__.__name__
            code = e.code
            description = e.description
            errMeg = "{}:  {}".format(exception_name, description)
            err = RestException(errMeg, code)
        log('error', repr(e), e)
        return err
    except:
        print("未知异常！")
        return  '未知异常', 200


def register_routes(app):
    app.register_blueprint(routes_index)
    app.register_blueprint(routes_user, url_prefix='/user')
    app.register_blueprint(routes_todo, url_prefix='/v1/todo')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'super secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    print('server run')
    # app = configured_app()
    config = dict(
        threaded=True,
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
