import arcpy

""" 
    Set the path of the input data roads and source data. You need to change to your own path.
    In this sample, the workspace is a geodatabase. 
    "bearMove" and "roads" are two feature classes in the geodatabase.
"""
#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\bookSampleData.gdb"
# ensure bearMove is in workspace first
arcpy.management.MakeFeatureLayer("bearMove","inferLy")
arcpy.management.MakeFeatureLayer("roads","targetLy")

""" 
    "MakeFeatureLayer_management" can create a feature layer object from the path of the input,
    which is a string.  "SelectLayerByAttribute", "Clip_analysis", and "Statistics_analysis" are
    then conducted on the feature layer.
""" 
for i in range(0,8):
    # select the polygon with FID = i
    arcpy.management.SelectLayerByAttribute("inferLy","NEW_SELECTION","\"OBJECTID \"="+str(i))
    # execute clip analysis and out intermediate data "out_" + str(i) in workspace
    fc = arcpy.analysis.Clip("targetLy","inferLy","out"+str(i))
    # execute sum statistical analysis and output result "sum_" + str(i) in workspace
    arcpy.analysis.Statistics(fc, "sum" + str(i), [["Shape_Length","SUM"]])
