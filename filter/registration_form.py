from wtforms import StringField, PasswordField, Form
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
from filter import Validator



class LoginForm(Validator):
    username = StringField('username', [validators.required(), validators.Length(min=2, max=25)])
    password = PasswordField('password', [validators.required(), validators.Length(min=6, max=20)])

class RegisgerForm(Validator):
    username = StringField('username', [validators.required(), validators.Length(min=2, max=25)])
    password = PasswordField('password', [validators.required(), validators.Length(min=6, max=20)])
