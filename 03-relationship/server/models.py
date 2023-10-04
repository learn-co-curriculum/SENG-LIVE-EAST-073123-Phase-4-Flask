from flask_sqlalchemy import SQLAlchemy
     
db = SQLAlchemy()

class Production(db.Model):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    title = db.Column(db.String) 
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    

class Actor(db.Model):
    __tablename__='actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Actor {self.id}, {self.name}>'


#1 $flask db init 
#2 $flask db migrate -m "message"
#3 $flask db upgrade head  