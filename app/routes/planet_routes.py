from flask import Blueprint
from ..models.planets import planets

planets_bp = Blueprint("planets_bp",__name__,url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    result_list = []

    for planet in planets:
        result_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            galaxy=planet.galaxy
        ))
    return result_list

    

