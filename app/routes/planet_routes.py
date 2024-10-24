from flask import Blueprint, make_response, abort
from ..models.planet import planets

planets_bp = Blueprint("planets_bp",__name__,url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict(),200
    

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        response = {"message": f"{planet_id} is not valid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet_id == planet.id:
            return planet
    
    response = {"message": f"{planet_id} is not found"}
    abort(make_response(response, 404))
