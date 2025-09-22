from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    db.init_app(app)

    from app import models

    with app.app_context():
        print('we are not creating the db yet')
        

    return app
