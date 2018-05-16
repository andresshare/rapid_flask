from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import  EmailField


class CommentForm(Form):
    username = StringField('username')
    email = EmailField('correo electronico')
    comment = TextField('comentario')


    