import arcpy

# set the workspace
#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp12data.gdb"
aspectly = arcpy.sa.Aspect("dem")
aspectly.save("aspect")
