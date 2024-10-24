from flask import Blueprint,abort,make_response
from ..models.planet import planets

planets_bp = Blueprint("planets_bp",__name__,url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "galaxy": planet.galaxy
            }
        )
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_plane(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "galaxy": planet.galaxy
    }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = f"message: planet {planet_id} invalid"
        abort(make_response(response,400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    response = f"message: planet {planet_id} not found"
    abort(make_response(response,404))