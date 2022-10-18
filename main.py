import math

"""class Courier
    def __init__(self, x, y):


class Order
    def __init__(self, x, y):"""

class Point:
    def __init__(self,x, y):
        self.x=x
        self.y=y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def __str__(self):
        return f"точка с координатами {self.x}, {self.y}"

    def get_distance(self, other_point):
        x1=self.x
        x2=other_point.x
        y1=self.y
        y2=other_point.y
        dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
        return dist

p1=Point(1,2)
p2=Point(7,2)
dist=p1.get_distance(p2)
print(dist)