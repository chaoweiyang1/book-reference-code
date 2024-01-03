import arcpy

#Please change this file path to your data location
workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data"

for dirpath, dirnames, filenames in arcpy.da.Walk(workspace):
    print("-------------")
    print(dirpath);
    print(dirnames);
    print(filenames);
    
