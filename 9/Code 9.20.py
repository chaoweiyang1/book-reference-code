import arcpy

# use the name of the coordinate system
spatialRef = arcpy.SpatialReference("Hawaii Albers Equal Area Conic")

# or use a projection file (.prj)
#Please change this file path to your data location
sr = arcpy.SpatialReference(r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data\states.prj")

print(spatialRef.name)
print(spatialRef.XYTolerance)
print(spatialRef.metersPerUnit)
print(spatialRef.GCS)
