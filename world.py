from typing import List
from sphere import Sphere
from vector import Vec

class World:
    def __init__(self):
        self.spheres: List[Sphere] = [
            # large dark plane, the ground
            #Sphere(Vec(0, -1000, 0), 0.001, 1000),
            # white sphere on the left
            Sphere(Vec(-2, 1, -2), 1, 1),
            # grey sphere in the center
            Sphere(Vec(0, 1, 0), 0.5, 1),
            # black sphere on the right
            Sphere(Vec(2, 1, -1), 0.1, 1),
        ]
        self.lights: List[Sphere] = [
            Sphere(Vec(0, 100, 0), 0.4, 0),
            Sphere(Vec(100, 100, 200), 0.5, 0),
            Sphere(Vec(-100, 300, 100), 0.1, 0)
        ]