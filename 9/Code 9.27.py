import arcpy

#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data"

"""
	"MakeFeatureLayer_management" can create a feature layer object from the path of the input
	data, which is a string.  Selection will be conducted on the feature layer.
"""
arcpy.management.MakeFeatureLayer("interstates.shp", "roadLy")
arcpy.management.MakeFeatureLayer("railway.shp", "railLy")

# select the features in the interstates layer, which intersect with the features in the railway layer
arcpy.management.SelectLayerByLocation("roadLy","INTERSECT","railLy",selection_type="NEW_SELECTION")
