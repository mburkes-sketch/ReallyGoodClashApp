from flask_login import UserMixin
from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

class User(db.Document, UserMixin):
    # user info (from registration form)
    username = db.StringField(required=True, unique=True, min_length=1, max_length=40)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    player_tag = db.StringField(required=True, min_length=3, max_length=15)

    def get_id(self):
        return self.username

class Deck(db.Document):
    # Links deck to user who created it
    author = db.ReferenceField(User, required=True)
    title = db.StringField(required=True, min_length=1, max_length=50)
    description = db.StringField(max_length=200)
    cards = db.ListField(db.StringField(), max_length=8, min_length=8, required=True)     # stores 8 card IDs as list of strings