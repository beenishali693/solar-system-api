from flask import Blueprint
from ..models.planets import planets

planets_bp = Blueprint("planets",__name__,url_prefix="/planets")

@planets_bp.get("")
def get_planets():
    return planets

