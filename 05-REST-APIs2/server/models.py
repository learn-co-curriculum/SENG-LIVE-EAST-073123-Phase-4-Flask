from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy


#configuring a MetaData
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
#"fk":foreign key constraints 


db = SQLAlchemy(metadata = metadata)


class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    #add rules to avoid accidental recursion
    serialize_rules = ("-roles.actor",)

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String) 
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)

   # Relationship mapping the production to related roles
    roles = db.relationship('Role', back_populates='production',cascade='all, delete-orphan')
    #back_populates attribute: bidirectional relationship  

    actors = association_proxy("roles", "actor")

    def __repr__(self):
        return f'<Production {self.id}, {self.title}>'

    

class Actor(db.Model, SerializerMixin):
    __tablename__="actors"
    
    serialize_rules = ("-roles.production",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

   # Relationship mapping the actor to related projects
    roles = db.relationship(
        'Role', back_populates='actor', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Actor {self.id}, {self.name}>'


class Role(db.Model, SerializerMixin):
    __tablename__ = "roles"

    serialize_rules = ("-production.roles", "-actor.roles",)

    id = db.Column(db.Integer, primary_key=True)

    charactor_name = db.Column(db.String)

    # Foreign key to store the production id
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    
   # Foreign key to store the actor id
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))

    # Relationship mapping the role to related actor
    actor = db.relationship('Actor', back_populates='roles')
    #back_populates attribute : a bidirectional relationship 


    # Relationship mapping the role to related production
    production = db.relationship('Production', back_populates='roles')

    def __repr__(self):
        return f'<Assignment {self.id}, {self.charactor_name}, {self.actor.name}, {self.production.title}'



#1 $flask db init 
#2 $flask db migrate -m "message"
#3 $flask db upgrade head  