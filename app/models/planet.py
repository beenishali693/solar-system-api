from flask import Flask

class Planet:

    def __init__(self,id,name,description,galaxy):
        self.id = id
        self.name = name
        self.description = description
        self.galaxy = galaxy
 
planets = [
    Planet(1,"Mercury","first planet from the sun","Milkyway"),
    Planet(2,"Venus","second planet from the sun, hottest planet","Milkyway"),
    Planet(3,"Earth","HOME PLANET","Milkyway"),
    Planet(4,"Mars","has the highest mountain","Milkyway"),
    Planet(5,"Jupiter","has many moons","Milkyway"),
    Planet(6,"Saturn","has many rings","Milkyway"),
    Planet(7,"Uranus"," the coldest planet in our Solar System","Milkyway"),
    Planet(8,"Neptune","the farthest planet from the Sun","Milkyway") 
]
