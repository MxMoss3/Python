import math
from graphics import *

sides = int(input("How many sides"))

def polygon(sides, radius):
    wedge_angle = 360 / sides

    points = [(radius * math.cos(math.radians(wedge_angle) * i),
        radius * math.sin(math.radians(wedge_angle) * i)) 
        for i in range(sides)]
    
    return points

print(polygon(sides, 10))
#win = GraphWin("Shape Spiral", 800, 800)


