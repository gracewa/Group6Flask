from flask import Flask
from flask_login import LoginManager
from config import DevConfig
from flask_uploads import UploadSet,configure_uploads,IMAGES

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

photos = UploadSet('photos',IMAGES)



bootstrap = Bootstrap()
db = SQLAlchemy()


# Creating the app configurations

app = Flask(__name__, instance_relative_config=True)

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing flask extensions
db.init_app(app)

# Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

