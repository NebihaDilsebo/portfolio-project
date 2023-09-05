from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Nebiha:Nur_muktar1@localhost/Fashion'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

