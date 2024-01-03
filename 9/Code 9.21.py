import arcpy
#Please change this file path to your data location
arcpy.env.workspace = (r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data")
# use the name of the coordinate system
spatialRef = arcpy.SpatialReference("Hawaii Albers Equal Area Conic")
# create the FDS using the spatialRef created from arcpy.SpatialReference() method
#Please change this file path to your data location
arcpy.management.CreateFeatureDataset(r'F:\GMU\stcenter\repositories\ArcGISdata\Default.gdb', 'results', spatialRef)

