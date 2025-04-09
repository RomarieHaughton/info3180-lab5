from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
csrf = CSRFProtect(app) #add csrf protection.

def create_app():
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import views

    return app

create_app()

with app.app_context():
    db.create_all()