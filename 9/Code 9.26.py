import arcpy

#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data"

"""
	Add fields "centX", "centY", "polyArea", and "polyPeri" to record the calculated results.
	"DOUBLE" is the value type, 20 is the precision of the double type, and 10 is the scale.
"""
arcpy.management.AddField("states.shp","centX","DOUBLE",20,10)
arcpy.management.AddField("states.shp","centY","DOUBLE",20,10)
arcpy.management.AddField("states.shp","polyArea","DOUBLE",20,6)
arcpy.management.AddField("states.shp","polyPeri","DOUBLE",20,6)

"""
	Calculate the centroid, area, and perimeter using the CalculateField_management tool.  "PYTHON_9.3"
	means the calculation expression "!SHAPE.CENTROID.X" is in Python 9.3 syntax.
"""
arcpy.management.CalculateField("states.shp","centX","!SHAPE.CENTROID.X!","PYTHON_9.3")
arcpy.management.CalculateField("states.shp","centY","!SHAPE.CENTROID.Y!","PYTHON_9.3")
arcpy.management.CalculateField("states.shp","polyArea","!SHAPE.AREA!","PYTHON_9.3")
arcpy.management.CalculateField("states.shp","polyPeri","!SHAPE.LENGTH!","PYTHON_9.3")
