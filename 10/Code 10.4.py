import arcpy

# set workspace #Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp10data\chp10data.gdb"

# describe spatial extent of dataset and calculate area
desc = arcpy.Describe("classifiedLandcover")
area = desc.width * desc.height