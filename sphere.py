from vector import Vec
from vector import Ray
import math

class Sphere:
    def __init__(self, center: Vec, color: float, radius: float):
        self.center: Vec = center
        self.color: float = color
        self.radius: float = radius
    
    def intersect(self, ray: Ray):
        # ray origin to center vector
        p: Vec = ray.origin.subtract(self.center)

        # dir * dir
        a: float = ray.direction.dot(ray.direction) 

        # 2 * (p 'dot' direction)
        b = 2 * p.dot(ray.direction)

        # p^2 - r^2
        c = p.dot(p) - self.radius * self.radius

        # d = b^2 - 4ac
        d = b * b - 4 * a * c

        if (d < 0):
            # No intersection
            return None
        
        sqrd = math.sqrt(d)
        distance = (-b - sqrd) / (2 * a)
        if (distance > 0.1):
            return distance
    
        distance = (-b + sqrd) / (2 * a)
        if (distance > 0.1):
            return distance

        # No intersection
        return None
