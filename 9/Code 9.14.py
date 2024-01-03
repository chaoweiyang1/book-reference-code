import arcpy

# list the field of the data "roads.shp" under the folder "ArcGISdata"
#Please change this file path to your data location
fieldlists = arcpy.ListFields(r"F:\GMU\stcenter\repositories\ArcGISdata\bookSampleData.gdb\roads")

# observe each field in the returning list
for field in fieldlists:
    # print out the property of the field, its name, scale, and type
    print(field.name,field.scale,field.type)
