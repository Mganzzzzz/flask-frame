from wtforms import Form, BooleanField, StringField, PasswordField, validators
from exception.form_valid_fali import FormValidFail
from flask import request
class Validator(Form):
    # username = StringField('Username', [validators.Length(min=4, max=25)])
    # email = StringField('Email Address', [validators.Length(min=6, max=35)])
    # password = PasswordField('New Password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message='Passwords must match')
    # ])
    # confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    #
    # fields = []
    # rules = []



    # def __init__(self):
    #     super().__init__()
    #     form = request.form
    #     self.validate_form()
    #     print('form', form)


    def validate_form(self):
        pass
        rules = self.rules
