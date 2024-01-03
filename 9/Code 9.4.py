import arcpy

#Please change this file path to your data location
inputdata = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data\Partial_Streets.shp"
with arcpy.da.SearchCursor(inputdata, ["Shape_Leng", "NAME", "TYPE"]) as rows:
    for row in rows:
        print("{}, {}, {}\n".format(row[0], row[1], row[2]))
