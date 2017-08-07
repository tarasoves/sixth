import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base Configuration"""
    DEBUG = False
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')


class TestingConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production Configuration"""
    DEBUG = False
    SECRET_KEY = 'my_precious'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
