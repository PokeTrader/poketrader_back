from project import db

class User(db.Model):
    username = db.Column(db.String(80), primary_key=True, unique=True)
    password = db.Column(db.String(200), nullable=False)