from flask import Flask
from flask_testing import TestCase

from project import db, jwt
from project.api.users.routes import users_blueprint


class BaseTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)

        app.config.from_object('project.config.TestingConfig')

        db.init_app(app)
        jwt.init_app(app)

        app.register_blueprint(users_blueprint)

        return app
    
    def setUp(self):
        db.create_all()
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()