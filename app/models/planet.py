from flask import Flask

class Planet:

    def __init__(self,id,name,description,galaxy):
        self.id = id
        self.name = name
        self.description = description
        self.galaxy = galaxy

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "galaxy": self.galaxy
            }


mercury = Planet(1,"Mercury","first planet from the sun","Milkyway")
venus = Planet(2,"Venus","second planet from the sun, hottest planet","Milkyway")
earth = Planet(3,"Earth","HOME PLANET","Milkyway")
mars = Planet(4,"Mars","has the highest mountain","Milkyway")
jupiter = Planet(5,"Jupiter","has many moons","Milkyway")
saturn = Planet(6,"Saturn","has many rings","Milkyway")
uranus = Planet(7,"Uranus"," the coldest planet in our Solar System","Milkyway")
neptune = Planet(8,"Neptune","the farthest planet from the Sun","Milkyway") 

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
