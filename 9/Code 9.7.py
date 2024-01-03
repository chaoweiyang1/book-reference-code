import arcpy

#Please change this file path to your data location
inputdata = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data\Partial_Streets.shp"

with arcpy.da.SearchCursor(inputdata, ["SHAPE@"], "FID < 10") as rows:
    for row in rows:
        for pntarray in row[0]:
            for pnt in pntarray:
                # return a tuple of x and y coordinates of the first two
                # features in the data
                print("{0}, {1}".format(pnt.X, pnt.Y))