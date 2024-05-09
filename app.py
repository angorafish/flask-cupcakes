from flask import Flask
from models import db, Cupcake, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cupcakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
connect_db(app)