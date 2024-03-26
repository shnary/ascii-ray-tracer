from math import sqrt

class Vec:
    def __init__(self, x=0, y=0, z=0):
        self.x: float = x
        self.y: float = y
        self.z: float = z
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z
        return self
    
    def subtract(self, vec):
        self.x -= vec.x
        self.y -= vec.y
        self.z -= vec.z
        return self

    def dot(self, vec) -> float:
        return self.x * vec.x + self.y * vec.y + self.z * vec.z
    
    def length(self) -> float:
        return sqrt(self.dot(self))

    def unit(self):
        unit_vec = Vec(self.x, self.y, self.z)
        unit_vec.x = unit_vec.x / unit_vec.length()
        unit_vec.y = unit_vec.y / unit_vec.length()
        unit_vec.z = unit_vec.z / unit_vec.length()
        return unit_vec


class Ray:
    def __init__(self, origin, direction):
        self.origin: Vec = origin
        self.direction: Vec = direction
