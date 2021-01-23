from project import db

class User(db.Model):
    __tablename__ = "user"

    username = db.Column(db.String(80), primary_key=True, unique=True)
    password = db.Column(db.String(200), nullable=False)

    trades = db.relationship("Trade", back_populates="user")