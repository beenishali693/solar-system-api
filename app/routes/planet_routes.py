from flask import Blueprint, make_response, abort, request, Response
from app.models.planet import Planet
from ..db import db
from .route_utilities import validate_model
planets_bp = Blueprint("planets_bp",__name__,url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    
    try:
        new_planet = Planet.from_dict(request_body)

    except KeyError as e:
        response = {"message": f"Invalid request: missing {e.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
    return response, 201
    

@planets_bp.get("")
def get_all_planets():

    query = db.select(Planet)
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    galaxy_param = request.args.get("galaxy")
    if galaxy_param:
        query = query.where(Planet.galaxy.ilike(f"%{galaxy_param}%"))

    #query = query.order_by(Planet.id)
    planets = db.session.scalars(query.order_by(Planet.id))

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet,planet_id)
    return planet.to_dict()

@planets_bp.get("/count")
def get_count():
    query = db.session.query(Planet.name).count()
    return {"count" : query}

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet,planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.galaxy = request_body["galaxy"]

    db.session.commit()

    return Response(status=204, mimetype="application/json") 

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet,planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")  

