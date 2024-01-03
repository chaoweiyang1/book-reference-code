import arcpy

#Please change this file path to your data location
inputdata = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data\railway.shp"

# create update cursor for the feature class
with arcpy.da.UpdateCursor(inputdata, ["Shape", "FID"]) as rows:
    for row in rows:
        if row[1] < 10:
            rows.deleteRow()
