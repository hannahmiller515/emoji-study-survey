# app/__init__.py

# third-party imports
from flask import Flask
from sqlalchemy import create_engine
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

# db variable initialization
engine = None

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)

    global engine
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],pool_size=20)
    from app import models

    from .survey import survey as survey_blueprint
    app.register_blueprint(survey_blueprint)
    
    return app