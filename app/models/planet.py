from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    galaxy: Mapped[str]

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "galaxy": self.galaxy
            }
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name=planet_data["name"],
            description=planet_data["description"],
            galaxy=planet_data["galaxy"]
        )
