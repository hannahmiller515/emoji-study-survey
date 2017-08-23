# app/__init__.py

# third-party imports
from flask import Flask
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

# db variable initialization
mysql = MySQL()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    Bootstrap(app)
    
    mysql.init_app(app)
    from app import models

    from .survey import survey as survey_blueprint
    app.register_blueprint(survey_blueprint)
    
    return app