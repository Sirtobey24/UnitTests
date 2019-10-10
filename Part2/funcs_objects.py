import math
from Part2.objects import *

p1 = Point(x=0, y=0)
p2 = Point(x=0, y=0)

c1 = Circle(x=0, y=0, r=0)
c2 = Circle(x=0, y=0, r=0)

distanceofcenterpts = math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def circles_overlap(c1, c2):
    return distanceofcenterpts < (c1.r + c2.r)
