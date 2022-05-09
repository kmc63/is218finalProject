"""A simple flask web app"""
import os

import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_mail import Mail

from app.auth import auth
from app.simple_pages import simple_pages
from app.cli import create_database
from app.db import database
from app.db import db
from app.db.models import User
from app.error_handlers import error_handlers
from app.logging_config import log_con, LOGGING_CONFIG
from app.context_processors import utility_text_processors
from app.transactions import transactionB

mail = Mail()

login_manager = flask_login.LoginManager()

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if os.environ.get("FLASK_ENV") == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif os.environ.get("FLASK_ENV") == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif os.environ.get("FLASK_ENV") == "testing":
        app.config.from_object("app.config.TestingConfig")
    app.mail = Mail(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    csrf = CSRFProtect(app)

    bootstrap = Bootstrap5(app)
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.register_blueprint(database)
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.register_blueprint(transactionB)
    app.context_processor(utility_text_processors)
    app.cli.add_command(create_database)
    db.init_app(app)

    api_v1_cors_config = {
        "methods": ["OPTIONS", "GET", "POST"],
    }
    CORS(app, resources={"/api/*": api_v1_cors_config})

    return app

@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
