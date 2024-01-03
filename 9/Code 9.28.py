import arcpy

#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data"

arcpy.management.MakeFeatureLayer("states.shp", "stateLy")
arcpy.management.MakeFeatureLayer("amtk_sta.shp", "stationLy")

# select Virginia from the state layer first
arcpy.management.SelectLayerByAttribute("stateLy","NEW_SELECTION",'"STATE_NAME"=\'Virginia\'')

# then select the railway stations (points) completely within Virginia (polygon)
arcpy.management.SelectLayerByLocation("stationLy","COMPLETELY_WITHIN","stateLy",selection_type="NEW_SELECTION")
