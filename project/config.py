
import datetime
import os

class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=int(os.getenv('JWT_EXPIRATION')))
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
    

class ProductionConfig(BaseConfig):
    pass
