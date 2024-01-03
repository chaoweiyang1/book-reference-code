import arcpy
#Please change this file path to your data location
arcpy.env.workspace = (r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data")
desc = arcpy.Describe('school.shp')
spatialRef = desc.SpatialReference

# create the FDS using the describe object's SR(SpatialReference) object
#Please change this file path to your data location
arcpy.management.CreateFeatureDataset(r'F:\GMU\stcenter\repositories\ArcGISdata\Default.gdb', 'results', spatialRef)

