from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .order import order

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

app.register_blueprint(order, url_prefix='/aga')

db = SQLAlchemy(app)