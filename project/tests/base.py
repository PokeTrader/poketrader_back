from flask import Flask
from flask_testing import TestCase

from project import db, ping


class BaseTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)

        app.config.from_object('project.config.TestingConfig')

        db.init_app(app)

        app.add_url_rule('/api/ping', 'ping', ping)

        return app
    
    def setUp(self):
        db.create_all()
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()