import os
import unittest

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


app_settings = os.getenv('APP_SETTINGS')
app = Flask(__name__)
app.config.from_object(app_settings)

db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)


from project.api.users.routes import users_blueprint
app.register_blueprint(users_blueprint)

@app.cli.command('test')
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0
    return 1
