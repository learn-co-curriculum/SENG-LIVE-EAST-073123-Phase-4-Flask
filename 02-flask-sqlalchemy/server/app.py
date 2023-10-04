from flask import Flask, jsonify, make_response, request 
from flask_migrate import Migrate
from models import db, Production


app = Flask(__name__) #Initialize the App
    

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'# Configure the database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)  # Set the migrations  

db.init_app(app) #initialize the application

#Routes    
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/lowest-budget-movies')
def get_lowest_budget_movies():
    movie = Production.query.order_by(Production.budget.desc()).first()
    prod = {
        "title": movie.title,
        "genre": movie.genre,
        "budget": movie.budget
    }
    return make_response(jsonify(prod), 200)

#dynamic route
@app.route('/productions/<string:title>')

def production(title):

    quer = Production.query.filter_by(title=title).first()
    production={
        "title": quer.title,
        "genre": quer.genre,
        "budget": quer.budget
    }
    return make_response(jsonify(production))
    # `make_response` will allow us to make a response object with the response body and status code
    # `jsonify` will convert our query into JSON

    # `@app.route('/productions/<string:title>')
    # def production(title):
    #     production = Production.query.filter(Production.title == title).first()
    #     production_response = {
    #         "title":production.title,
    #         "genre":production.genre,
    #         "director": production.director
    #         }
    #     response = make_response(
    #         jsonify(production_response),
    #         200
    #     )`    

# 16.✅ View the path and host with request context

@app.route("/context")
def context():
    import ipdb;
    # ipdb.set_trace()

    print("==========IN CONTEXT=======")
    return f'''
    <h1>
        path   :   {request.path}
    </h1>

    <h1>
        Host    :   {request.host}
    </h1>
    '''

# 17.✅ Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.
@app.before_request
def runs_before():
    cur_user = {"user_id": 3, "username": "spiderman"}
    print("------ BEFORE REQUEST ------", cur_user)

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

if __name__ == '__main__':
    app.run(port=5555, debug=True)