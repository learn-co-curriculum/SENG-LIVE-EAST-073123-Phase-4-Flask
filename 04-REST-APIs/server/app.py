from flask import Flask, jsonify, make_response, request 
from flask_migrate import Migrate
from models import db, Production, Actor, Role


from flask_restful import Api, Resource

app = Flask(__name__) #Initialize the App
    

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'# Configure the database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
#configures JSON responses to print on indented lines

migrate = Migrate(app, db)  # Set the migrations  

db.init_app(app) #initialize the application

api = Api(app) #initialize API

class Productions(Resource): #this function name should be different from model class name that we are importing
    #Create a route to /productions for GET requests
    def get(self):

        #Create the query
        quer = Production.query.all()

        #Loop through the query and convert each object into a dictionary 
        prods = []
        for each_p in quer:
            prods.append({
                "id": each_p.id,
                "title": each_p.title,
                "genre": each_p.genre,
                "budget": each_p.budget
            })

        #Use make_response and jsonify to return a response
        resp = make_response(jsonify(prods), 200)
 
        return resp
    

    def post(self):
        #Get information from request.get_json()
        request_json = request.get_json()
        
        #Create new object
        new_production = Production(
            title=request_json['title'],
            genre=request_json['genre'],
            budget=request_json['budget'],
            image=request_json['image'],
            director=request_json['director'],
            description=request_json['description'],
            ongoing=request_json['ongoing']
        )
        #Add and commit to db
        db.session.add(new_production)
        db.session.commit()

        #Convert to dictionary
        prod_dict = {
            "id": new_production.id,
            "title": new_production.title,
            "genre": new_production.genre,
            "budget": new_production.budget}

        #return as JSON
        response = make_response(jsonify(prod_dict),
            201
        )

        return response
    
api.add_resource(Productions, '/productions')
#Test in Postman

if __name__ == '__main__':
    app.run(port=5555, debug=True)
#run `python app.py`
#application as a script instead of using `flask run`