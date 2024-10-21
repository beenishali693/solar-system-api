from flask import Blueprint
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

