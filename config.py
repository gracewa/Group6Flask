import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = "anystring"


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings


    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:g11111111@localhost/bookreviews'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:g11111111@localhost/bookreviews'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
