import arcpy

#Please change this file path to your data location
arcpy.env.workspace = r'F:\GMU\stcenter\repositories\ArcGISdata\chp11data'

routeLy = arcpy.na.MakeRouteLayer(in_network_dataset = "roads_ND.nd", out_network_analysis_layer =
"myRoute", impedance_attribute = "Length", find_best_order = "FIND_BEST_ORDER",
ordering_type = "PRESERVE_BOTH", time_windows = "NO_TIMEWINDOWS",
accumulate_attribute_name = "Length", UTurn_policy = "ALLOW_UTURNS", restriction_attribute_name = "#",
hierarchy = "NO_HIERARCHY", hierarchy_settings = "#",
output_path_shape = "TRUE_LINES_WITH_MEASURES", start_date_time = "#").getOutput(0)


# get the sub classes of the route layer 
naClasses = arcpy.na.GetNAClassNames(routeLy, "INPUT")