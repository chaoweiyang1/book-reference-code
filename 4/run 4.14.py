import math

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def getDistance(self, other): # Declare getDistance as a method
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

# Declare four points
p0, p1,p2,p3 = Point(), Point(1,5), Point(2,8), Point(10,3)
# Keep in a list
points = [p0, p1, p2, p3]
# Declare the biggestDistance variable
biggestDistance = 0.0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        currentDistance = points[i].getDistance(points[j])
    if currentDistance > biggestDistance:
        biggestDistance = currentDistance

# Finish finding and print biggest distance
print('Biggest distance is ->', biggestDistance)
# Output: Biggest distance is -> 10.44030650891055