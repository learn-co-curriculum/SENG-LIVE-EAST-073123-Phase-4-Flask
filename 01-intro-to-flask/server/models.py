# 📚 Review With Students:
    # Review models
    # Review MVC
#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # save SQLAlchemy flask in db variable

# create a Production Model
class Production(db.Model): #take in sqlalchemy db as an arg
    __tablename__ = "productions" # set table name 

    id = db.Column(db.Integer, primary_key=True)  #set primary key 

    created_at = db.Column(db.DateTime, server_default=db.func.now()) 
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #columns
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)

# 1. ✅ Create a Production Model
	# tablename = 'Productions'
	# Columns:
        # title: string, 
        # genre: string, 
        # budget:float, '
        # image:string,
        # director: string, 
        # description:string, 
        # ongoing:boolean, created_at:date time, updated_at: date time 
# 2. ✅ navigate to app.py