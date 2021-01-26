import os
import unittest

from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()


app_settings = os.getenv('APP_SETTINGS')
app = Flask(__name__)
app.config.from_object(app_settings)

db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

CORS(app)

from project.api.users.routes import users_blueprint
from project.api.pokemons.routes import pokemons_blueprint
from project.api.trades.routes import trades_blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(pokemons_blueprint)
app.register_blueprint(trades_blueprint)

from project.api.users.models import User
from project.api.trades.models import Trade, TradeGroup, TradePokemon

@app.cli.command('test')
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0
    return 1
