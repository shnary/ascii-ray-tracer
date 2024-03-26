
import vector
from world import World
from vector import Vec, Ray

HEIGHT = 25
WIDTH = 50

def trace(world: World, origin: Vec, direction: Vec):
    index = -1;       # nearest sphere index
    distance = 0; # nearest sphere distance

    for i in range(len(world.spheres)):
        # Loop over every sphere, find nearest non-NAN intersection
        d = world.spheres[i].intersect(Ray(origin, direction))
        if (d is not None and (index < 0 or d < distance)):
            distance = d
            index = i

    if (index < 0):
        return 0; # If no intersection: return black color
    
    # If there is a sphere - return white color
    return 1

def render(world: World, width: int, height: int):
    for y in range(height):
        for x in range(width):
            direction = Vec(x - width / 2, height / 2 - y, -height).unit()
            # c would be the color of the pixel
            c = trace(world, Vec(0, 1, 5), direction)
            # find the suitable ASCII symbol "density" from 0 to 10
            pixel = " .:-=+*#%@$"[(int)(c * 10)]
            print(pixel, end='')
            print(pixel, end='')
        print("\n")

def main():
    render(World(), WIDTH, HEIGHT)

if "__main__" == __name__:
    main()