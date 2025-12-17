from ast import Pass
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import (
    InputRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
)


from .models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=40)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password")])
    player_tag = StringField("Clash Royale Player Tag", validators=[InputRequired()])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")

class PlayerLookupForm(FlaskForm):
    player_tag = StringField("Player Tag (e.g., #YP9JJPJLY)", validators=[InputRequired(), Length(min=3, max=15)])
    submit = SubmitField("Search Player")

class MakeADeck(FlaskForm):
    title = StringField("Deck Name", validators=[InputRequired(), Length(min=1, max=50)])
    description = TextAreaField("Strategy / Notes", validators=[Length(max=200)])
    submit = SubmitField("Save Deck")