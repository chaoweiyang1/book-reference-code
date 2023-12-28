import random

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

# 2. Declare the Rectangle class
class Rectangle:
    def __int__(self):
        ## A rectangle can be determined by (minX, maxX) (minY, maxY)
        self.minX = self.minY = 0.0
        self.maxX = self.maxY = 1.0
    def contains(self, point): ## Check if a point is within a rectangle
        pass  ## Implement me

# 3. Generate four points
# Define a Point list to keep four points
points = []
# Generate four points and append to the points list
pass # IMPLEMENT ME

# 4. Generate four rectangles
# Define a Rectangle list
rects = []
for i in range(4):
    rectangle = Rectangle()
    # Generate x
    x1 = random.random()
    x2 = random.random()
    # Ensure x1 != x2
    while(x1 == x2):
        x1 = random.random()
    if x1 < x2:
        rectangle.minX = x1
        rectangle.maxX = x2
    elif x1 > x2:
        rectangle.minX = x2
        rectangle.minY = x1
    # Develop codes to generate y values
    # Ensure the rectangle is not a line below
    pass # IMPLEMENT ME
    rects.append(rectangle)

# 5. Add code to check which point is in which rectangle
    resultList = []
    pass # IMPLEMENT ME

# 6. write the results to file
f = open(r'F:\GMU\stcenter\repositories\book-reference-code\5\HM5_Result.txt','w') # Change path as needed
for result in resultList:
    f.write(result + '\n')
f.close()