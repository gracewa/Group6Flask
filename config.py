import os
import cloudinary


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = "anystring"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #cloudinary configuration
    cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME')
    api_key = os.environ.get('CLOUDINARY_API_KEY')
    api_secret = os.environ.get('CLOUDINARY_API_SECRET')

    cloudinary.config(cloud_name='group6flask', api_key='771748118468722',
                      api_secret='Uye0Bi1UGZRvFNO8O8viekFqqIE')


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

'''
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
'''
