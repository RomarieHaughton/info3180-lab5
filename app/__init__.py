from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__) # Create the Flask app here

def create_app():
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import views after app is configured
    from app import views

    return app

create_app() # Configure the app

with app.app_context(): #create app context and create all tables.
    db.create_all()