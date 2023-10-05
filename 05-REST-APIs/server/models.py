from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
#add serializer to get association / be able to use to_dict() method in app.py
from sqlalchemy.ext.associationproxy import association_proxy

#configuring a MetaData object for a database using SQLAlchemy
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
#"fk":foreign key constraints 
# table name, column name, and referred table name.

db = SQLAlchemy(metadata = metadata)


class Production(db.Model, SerializerMixin): #add serializer as the second arg

    __tablename__ = "productions"

    serialize_rules = ("-roles.actor",) #add rules to avoid accidental recursive serializing

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
    #back_populates attribute is used to define a bidirectional relationship between two tables or models
    #back_populates:how changes made to one side of the relationship should be reflected on the other side. 

    #delete-orphan: when an object is removed (deleted) from the parent's collection of related objects, SQLAlchemy should also consider that the removed object is orphaned and should be deleted from the database.

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
        #back_populates attribute is used to define a bidirectional relationship between two tables or models
        #back_populates:how changes made to one side of the relationship should be reflected on the other side. 

        #delete-orphan: when an object is removed (deleted) from the parent's collection of related objects, SQLAlchemy should also consider that the removed object is orphaned and should be deleted from the database.

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
    #back_populates attribute is used to define a bidirectional relationship between two tables or models
    #back_populates:how changes made to one side of the relationship should be reflected on the other side.


    # Relationship mapping the role to related production
    production = db.relationship('Production', back_populates='roles')

    def __repr__(self):
        return f'<Assignment {self.id}, {self.charactor_name}, {self.actor.name}, {self.production.title}'


#1 $flask db init 
#2 $flask db migrate -m "message"
#3 $flask db upgrade head  