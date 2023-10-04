from app import app
from models import Production, db
from faker import Faker # adding faker
from random import choice as rc

with app.app_context():

    Production.query.delete()

    fake = Faker() # create and init a faker generator
    prod_list = [] # empty list

    genres = ["action", "adventure", "comedy", "drama", "fantasy"]

    #add production instances to the list
    for n in range(29):
        prod = Production(
            title=fake.catch_phrase(),
            genre=rc(genres),
            image=fake.image_url(),
            budget=rc([100, 200, 300, 50, 25, 0]),
            director=fake.name(),
            ongoing=rc([True, False]),
            description=fake.catch_phrase()
        )
        prod_list.append(prod)


    amsterdam = Production(
       title="amsterdam",
       genre="mystery",
       image="https://m.media-amazon.com/images/M/MV5BNDQwNzE0ZTItYmZjMC00NjI3LWFlNzctNTExZDY2NWE0Zjc0XkEyXkFqcGdeQXVyMTA3MDk2NDg2._V1_FMjpg_UX1000_.jpg",
       budget=134,
       director="david o russell",
       ongoing=True,
       description="let the love, murder, and conspiracy begin"
    )

    nope = Production(
       title='nope',
       genre='sci-fi',
       image='https://m.media-amazon.com/images/M/MV5BOGJhYzAwN2MtNjA1Ny00ZjJiLWFmNzYtMDgzNTUzYjc5NTIzXkEyXkFqcGdeQXVyMTUzOTcyODA5._V1_.jpg',
       budget=130,
       director='jordan peele',
       ongoing=False,
       description='nope'
    )

    db.session.add_all([amsterdam, nope])
    db.session.add_all(prod_list)
    db.session.commit()