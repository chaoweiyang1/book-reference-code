>>> bIntersect = False
>>> def intersect(line1,line2):
        for i in range(len(line1.lineSegments)):
            for j in range(len(line2.lineSegments)):
                if (line1.lineSegments[i].segIntersect(line2.lineSegments[j])):
                    bIntersect = True
                    break
