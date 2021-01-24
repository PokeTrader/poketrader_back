from flask import Flask
from flask_testing import TestCase
from flask_jwt_extended import create_access_token

from project import db, jwt
from project.api.users.routes import users_blueprint
from project.api.trades.routes import trades_blueprint

from project.api.users.models import User


class BaseTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)

        app.config.from_object('project.config.TestingConfig')

        db.init_app(app)
        jwt.init_app(app)

        app.register_blueprint(users_blueprint)
        app.register_blueprint(trades_blueprint)

        return app

    def create_token(self, identity='someuser'):
        token = create_access_token(identity=identity)
        headers = {
            'Authorization': 'Bearer %s' % token
        }
        return headers

    def create_user(self, username='someuser'):
        user = User()
        user.username = username
        user.password = 'somepass'
        db.session.add(user)
        db.session.commit()

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()