class Point:
    def __init__(self, x=0, y=0, name=''):
        self.x = x
        self.y = y
        self.name = name
    def setName(self,name):
        self.name = name


point0 = Point()
point1 = Point(1,1,'first point')
print(point0.x, point0.y, point0.name)
# Output: 0 0 ''
print(point1.x, point1.y, point1.name)
# Output: 1 1 first point
point1.setName('second point')
print(point1.name)
# Output: second point
