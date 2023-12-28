import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dis(self,point):
        return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)

f = open(r'F:\GMU\stcenter\repositories\book-reference-code\4\code 4.18 data.txt','r') # Change path as needed
print(f.readline())

i = 0
points = []
while (i==0):
    line = f.readline()
    if (line.find(':') != -1):
        cords = line.split(':')[1]
        if (cords.find(',') != -1):
            xy = cords.split(',')
            points.append(Point(float(xy[0]), float(xy[1])))
    else:
        i = 1

outf = open(r'F:\GMU\stcenter\repositories\book-reference-code\4\results4.18.txt','w') # change path as needed
lpoints =[]
dis = 0
print(points)

for k in range(len(points)):
    for l in range(k + 1, len(points)):
        if (points[k].dis(points[l]) > dis):
            dis = points[k].dis(points[l])
            while (len(lpoints) > 0):
                lpoints.remove(lpoints[0])
            lpoints.append(points[k])
            lpoints.append(points[l])

outf.write('The longest distance is between point ['+str(lpoints[0].x)+','+str(lpoints[0].y)+'] and ' +
           'point ['+str(lpoints[1].x)+','+str(lpoints[1].y)+']\n The distance is '+str(dis))

outf.close()
f.close()