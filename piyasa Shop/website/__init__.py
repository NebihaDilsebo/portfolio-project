'''
Converts the website folder into a python package so that we can export data between files
'''
# Flask is used to create a quick website backend 
from flask import Flask
# timer
from datetime import timedelta


# Create the flask app
def create_app():
  # App configs
  app = Flask(__name__)
# set timer for session data
  app.permanent_session_lifetime = timedelta(days=3)

  return app
