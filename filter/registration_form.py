# from . import *
#
# class LoginForm(Validator):
#     username = StringField('username', [validators.Length(min=4, max=25)])
#     # password = PasswordField('password', [
#     #     validators.Length(min=8, max=12)
#     # ])
#     pass


from wtforms import Form, BooleanField, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    # email = StringField('Email Address', [validators.Length(min=6, max=35)])
    # password = PasswordField('New Password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message='Passwords must match')
    # ])
    # confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
