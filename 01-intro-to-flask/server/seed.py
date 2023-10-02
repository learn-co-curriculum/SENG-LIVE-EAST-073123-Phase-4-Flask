#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models
from app import app
from models import Production, db

# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`


# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
    Production.query.delete()
    #create some seeds for the production table
    amsterdam = Production(
        title="amsterdam",
        genre="mystery",
        image="jpeg",
        budget=120,
        director = "david",
        description = "amsterdam,",
        ongoing = True
    )
    
    nope = Production(
        title="nope",
        genre = "sci-fi",
        image="jpeg",
        budget=100,
        director="Jordan Peele",
        description = "nope",
        ongoing=False
    )

    db.session.add_all([amsterdam, nope])
    db.session.commit() 


# 8.✅ Create a query to delete all existing records from Production    
   
# 9.✅ Create some seeds for production and commit them to the database. 
# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  
    
    