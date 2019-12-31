import os
basedir = os.pathabs(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING =  False
    CSRF_ENABLED = True
    SECRET_KEY = 'esta-es-la-clave-secreta'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG =  False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG =  True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG =  True

class TestingConfig(Config):
    TESTING = True
