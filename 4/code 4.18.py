>>> import math
>>> class Point:
        def __init__(self,x,y):
                self.x = x
                self.y = y
        def dis(self,point):
                return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)
>>> f = open(r'C:\GMU\stcenter\repositories\book-reference-code\4\code 4.18 data.txt','r') # change path as needed
>>> f.readline()
'Text file content:\n'
>>> i = 0
>>> points = []
>>> while (i==0):
        line = f.readline()
        if (line.find(':')!=-1):
                cords = line.split(':')[1]
                if (cords.find(',')!=-1):
                        xy = cords.split(',')
                        points.append(Point(float(xy[0]),float(xy[1])))
        else:
                i=1
>>> outf = open(r'C:\GMU\stcenter\repositories\book-reference-code\4\results4.18.txt','w') # change path as needed
>>> lpoints = []
>>> dis = 0
>>> print(points)
[<__main__.Point object at 0x00000251D5B26B50>, <__main__.Point object at 0x00000251D5B15E50>, 
 <__main__.Point object at 0x00000251D5B14E90>, <__main__.Point object at 0x00000251D3C67110>, 
 <__main__.Point object at 0x00000251D5B26ED0>, <__main__.Point object at 0x00000251D5B23810>, 
 <__main__.Point object at 0x00000251D5B29990>, <__main__.Point object at 0x00000251D5B2ACD0>]
>>> for k in range(len(points)):
        for l in range(k+1, len(points)):
                if (points[k].dis(points[l])>dis):
                        dis = points[k].dis(points[l])
                        while (len(lpoints)>0):
                                lpoints.remove(lpoints[0])
                        lpoints.append(points[k])
                        lpoints.append(points[l])
>>> outf.write('The longest distance is between point ['+str(lpoints[0].x)+','+str(lpoints[0].y)+'] and ' +
           'point ['+str(lpoints[1].x)+','+str(lpoints[1].y)+']\n The distance is '+str(dis))
107
>>> outf.close()
>>> f.close()


