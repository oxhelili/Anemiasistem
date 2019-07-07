from datetime import datetime
from anemiasistem import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String, nullable=False)
    rbc = db.Column(db.Integer, nullable=False)
    hct = db.Column(db.Integer, nullable=False)
    hb = db.Column(db.Integer, nullable=False)
    mcv = db.Column(db.Integer, nullable=False)
    mch = db.Column(db.Integer, nullable=False)
    b12 = db.Column(db.Integer, nullable=True)
    af = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.name}', '{self.gender}','{self.rbc}','{self.hct}','{self.hb}','{self.mcv}','{self.mch}','{self.b12}','{self.af}')"