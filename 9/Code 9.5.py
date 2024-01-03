import arcpy

#Please change this file path to your data location
inputdata = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data\Partial_Streets.shp"

# select the features with FID < 10
with arcpy.da.SearchCursor(inputdata, ["Shape_Leng", "NAME", "TYPE"], "FID < 10") as rows:
    for row in rows:
        print("{}, {}, {}\n".format(row[0], row[1], row[2]))
