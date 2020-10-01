from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy

#from config import config_options


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
#photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()

if __name__ == '__main__':
    app.run()