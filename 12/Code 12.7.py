import arcpy

#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp12data.gdb"

# recreate flow direction on the dem with sinks filled
fd_filled = arcpy.sa.FlowDirection("dem_sinkfilled","NORMAL")
fd_filled.save("fd_filled")
# calculate the flow accumulation
fa = arcpy.sa.FlowAccumulation("fd_filled","","INTEGER")
fa.save("fa")