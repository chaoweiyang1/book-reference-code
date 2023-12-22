import math

class Feature:
    def __init__(self, name = ''):
        self.name = name

    def draw(self, map):
        pass


class Point(Feature):
    def __init__(self, x =0.0, y = 0.0):
        self.x = x
        self.y = y
    def calDis(self, point):
        return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)

p1 = Point(1,2)
p2 = Point(2,2)
print(p1.calDis(p2))
# Output: 1.0
