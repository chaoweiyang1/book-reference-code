import arcpy

#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp12data.gdb"

# calculate sink
sinks = arcpy.sa.Sink("fd")
# fill the sinks on dem
dem_sinkfilled = arcpy.sa.Fill("dem")
dem_sinkfilled.save("dem_sinkfilled")