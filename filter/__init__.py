from werkzeug.datastructures import ImmutableMultiDict
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, Regexp, URL, UUID
from exception.form_valid_fali import FormValidFail
from utils.utils import log


class Validator(Form):

    def __init__(self, form):
        super(Validator, self).__init__(form)
        # super(Validator, self).__init__(**body_data, **query_data)
        valid = self.validate()
        if valid:
            pass
        else:
            errors = self.errors
            raise FormValidFail(errorMsgs=errors)

            # raise FormValidFail('校验不通过')

if __name__ == '__main__':
    pass
    # form = [dict(username='12')]
    # log('debug form', form)
    form = ImmutableMultiDict([('username', '')])
    r = Validator(form)
    # r.validate()
    # print('r', r)
    # print(r.errors)
