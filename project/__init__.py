import os
import unittest

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


app_settings = os.getenv('APP_SETTINGS')
app = Flask(__name__)
app.config.from_object(app_settings)

db.init_app(app)
migrate.init_app(app, db)


@app.route('/api/ping')
def ping():
    return jsonify({
        'response': 'pong!'
    }), 200


@app.cli.command('test')
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0
    return 1
