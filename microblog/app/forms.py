from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    # DataRequired() checks that the field is not empty
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
