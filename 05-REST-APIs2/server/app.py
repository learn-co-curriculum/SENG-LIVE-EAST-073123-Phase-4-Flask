from flask import Flask, jsonify, make_response, request 
from flask_migrate import Migrate
from models import db, Production, Actor, Role
from flask_restful import Api, Resource
#importing flask_restful 

app = Flask(__name__) #Initialize the App

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'# Configure the database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
#configures JSON responses to print on indented lines

migrate = Migrate(app, db)  # Set the migrations  

db.init_app(app) #initialize the application

#initialize the API
api = Api(app)

#CRud
class Productions(Resource): #should be different from the model 

    #GET 
    def get(self):
        # #create a query
        # quer = Production.query.all()

        # # loop through the query and convert each obj into a dict
        # prods = []

        # for each_p in quer:
        #     prods.append({
        #         "id": each_p.id,
        #         "title": each_p.title,
        #         "genre": each_p.genre,
        #         "budget": each_p.budget
        #     })

        prods = [ production.to_dict() for production in Production.query.all() ]

        #return a response, add a status #
        resp = make_response(jsonify(prods), 200)

        return resp
    
    #post
    def post(self):
        request_json = request.get_json()

        # create a new object 
        new_production = Production(
            title=request_json['title'],
            genre = request_json['genre'],
            budget=request_json['budget']    
        )
        # add / commit to db
        db.session.add(new_production)
        db.session.commit()

        #convert to dictionary 
        prod_dict = {
            "id": new_production.id,
            "title": new_production.title,
            "genre": new_production.genre,
            "budget": new_production.budget
        }

        #return as JSON
        response = make_response(jsonify(prod_dict), 201)

        return response

api.add_resource(Productions, '/productions')

#cRuD
class ProductionsById(Resource):

    def get(self, id):
        #import ipdb; ipdb.set_trace()
        id_prod = Production.query.filter(Production.id == id).one_or_none()

        #handle message 
        if id_prod is None: 
            return make_response({"error": "Production Not Found"}, 404)
        
        id_prod_dict = {
            "id": id_prod.id,
            "title": id_prod.title,
            "genre": id_prod.genre,
            "budget": id_prod.budget
        }

        return make_response(id_prod_dict, 200)
    
    def delete(self, id):
        #import ipdb; ipdb.set_trace()
        id_prod = Production.query.filter_by(id=id).one_or_none()
        #filtering elements from iterable objects, 
        #filter_by is for ORM, SQLAlchemy. filters database based on attribute-value pairs 

        if id_prod: 
            db.session.delete(id_prod)
            db.session.commit()

            return make_response({"message": "deleted"}, 204)
        
        return make_response({"error": "Production Not Found"}, 404)

api.add_resource(ProductionsById, "/productions/<int:id>")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
#run `python app.py`
#application as a script instead of using `flask run`