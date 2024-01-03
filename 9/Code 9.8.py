import arcpy

#Please change this file path to your data location
inputdata = r"F:\GMU\stcenter\repositories\ArcGISdata\chp9data\Partial_Streets.shp"

# create update cursor for the feature class
with arcpy.da.UpdateCursor(inputdata, ["Shape_Leng", "FID"]) as rows:
	for row in rows:
		# update the field "Shape_Leng" under the conditions of field "FID"
		if row[1] > 10:
			row[0] = row[0] * 0.3048
		else:
			row[0] = row[0] * 0.5
		rows.updateRow(row)
