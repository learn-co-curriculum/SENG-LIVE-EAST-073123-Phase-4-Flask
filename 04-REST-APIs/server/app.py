from flask import Flask, jsonify, make_response, request 
from flask_migrate import Migrate
from models import db, Production, Actor, Role

app = Flask(__name__) #Initialize the App

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'# Configure the database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
#configures JSON responses to print on indented lines

migrate = Migrate(app, db)  # Set the migrations  

db.init_app(app) #initialize the application


if __name__ == '__main__':
    app.run(port=5555, debug=True)
#run `python app.py`
#application as a script instead of using `flask run`