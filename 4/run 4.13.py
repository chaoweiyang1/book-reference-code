import math

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def getDistance(self, other): # Declare getDistance as a method
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

# Declare three points
p1,p2,p3 = Point(1,5), Point(2,8), Point(10,3)

# Calculate the distances among random two points and keep them in a list
dist1 = p1.getDistance(p2)
dist2 = p1.getDistance(p3)
dist3 = p2.getDistance(p3)
distances = [dist1,dist2,dist3]

#Declare the biggestDistance variable
biggestDistance = 0.0
for i in range(len(distances)):
    currentDistance = distances[i]
    if currentDistance > biggestDistance:
        biggestDistance = currentDistance

# Finish finding and print biggest distance
print("Biggest distance is ->", biggestDistance)
# Output: Biggest distance is -> 9.433981132056603