import pytest
from app import create_app
from app.db import db
from app.models.planet import Planet
from flask.signals import request_finished
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def two_saved_planets(app):
    #Arrange
    earth = Planet(name="Earth",
    description="A vibrant blue and green planet, known for its diverse ecosystems and human inhabitants.",
    galaxy="Milky Way")
    mars = Planet(name="Mars",
    description="A cold, red planet with a thin atmosphere and known for its high mountains and deep valleys.",
    galaxy="Milky Way")

    db.session.add_all([earth,mars])
    db.session.commit()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()