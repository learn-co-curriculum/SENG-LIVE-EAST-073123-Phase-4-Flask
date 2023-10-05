from app import app
from models import Production, Actor, Role, db
from faker import Faker # adding faker
from random import choice as rc

with app.app_context():

    # Delete all rows in tables
    Production.query.delete()
    Actor.query.delete()
    Role.query.delete()
    db.session.commit()

    fake = Faker() # create and init a faker generator


    ########### P R O D U C T I O N #########################
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

    #generate multiple production
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





    ########### A C T O R #########################

    a1 = Actor(name = fake.name())

    a2 = Actor(name = fake.name())

    a3 = Actor(name = fake.name())

    a4 = Actor(name = fake.name())

    a5 = Actor(name = fake.name())

    a6 = Actor(name = fake.name())

    actor_list = []

    for n in range(20):
        act = Actor(
            name=fake.name()
        )
        actor_list.append(act)

    ########### R O L E #########################
    r1 = Role(
                charactor_name=fake.name(),
                actor=a1,
                production=nope)
    r2 = Role(
                charactor_name=fake.name(),
                actor=a2,
                production=amsterdam)
    r3 = Role(
                charactor_name=fake.name(),
                actor=a3,
                production=nope)
    
    r4 = Role(
                charactor_name=fake.name(),
                actor=a4,
                production=amsterdam)
    r5 = Role(
                charactor_name=fake.name(),
                actor=a5,
                production=amsterdam)
    r6 = Role(
                charactor_name=fake.name(),
                actor=a6,
                production=nope)
    
    

    db.session.add_all([amsterdam, nope])
    db.session.add_all(prod_list)
    db.session.add_all([r1, r2, r3])
    db.session.add_all(actor_list)

    # db.session.add_all([amsterdam, nope] + prod_list + [r1, r2, r3] + actor_list)

    db.session.commit()
