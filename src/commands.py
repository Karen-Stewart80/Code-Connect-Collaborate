from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Profiles import Profiles
    from faker import Faker
    faker = Faker()

    for i in range(20):
        profile = Profiles()
        profile.username = faker.name()
        profile.fname = faker.first_name()
        profile.lname = faker.last_name()
        profile.userpass = faker.password()
        profile.profile_pic=faker.text()
        profile.account_active=faker.boolean()
        profile.email= faker.email()
        profile.github=faker.text()
        db.session.add(profile)

    db.session.commit()
    print("Tables seeded")