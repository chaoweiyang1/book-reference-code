import math

class Points:
    def __init__(self, x=0.0, y=0.0):
        self.x,self.y = x, y

class Polyline:
    def __init__(self, points =[]):
        self.points = points
    def getLength(self):
        i = 0
        length =  0.0
        while i < len(self.points)-1:
            length += math.sqrt((self.points[i + 1].x - self.points[i].x) ** 2 +
                                (self.points[i + 1].y - self.points[i].y) ** 2)
            i += 1
        return length

# Function to read out data line by line
# Returns all points from both lines
# Returns two objects: points list and number of points from the first line
def readPolylineFile(fileName):
    f = open(fileName, 'r')
    polylines, points, index = [], [],0
    firstPolyLineNum = 0
    for line in f:
        index += 1
        if index == 1:
            continue
        coords = line.split(':')[1]
        eachcoords = coords.split(';')
        coordsLen = len(eachcoords)
        if index == 2:
            firstPolyLineNum = coordsLen-1
            print('The first polyline number is: ', firstPolyLineNum)
        for i in range(coordsLen-1):
            singlecoords = eachcoords[i]
            #print('singlecoords,', singlecoords)
            xCoord = singlecoords.split(',')[0]
            yCoord = singlecoords.split(',')[1]
            #print('xCoord and yCoord, ',  xCoord, yCoord)
            point = Points(float(xCoord),float(yCoord))
            points.append(point)
    f.close()
    return points, firstPolyLineNum

# Call the function to read data and put into points list
results = readPolylineFile(r'F:\GMU\stcenter\repositories\book-reference-code\4\polylinesHw4.txt') # change path as needed
points = results[0]
firstPolylinePointNum = results[1]
length = len(points)
print('The total points and the number of points for firstpolyline is:',\
      length, firstPolylinePointNum)

# Gets the points for first polyline and calculate length
pointsForFirstPoly = points[0:firstPolylinePointNum]
polyLine1 = Polyline(pointsForFirstPoly)
lengthForFirstPoly = polyLine1.getLength()
print("Length for first polyline -> ", lengthForFirstPoly)

# Gets the points for second polyline and calculate length
pointsForSecondPoly = points[firstPolylinePointNum:]
polyLine2 = Polyline(pointsForSecondPoly)
lengthForSecondPoly = polyLine2.getLength()
print("Length for Second polyline -> ", lengthForSecondPoly)
