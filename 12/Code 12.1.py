import arcpy

#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp12data.gdb"

"""
    DEM to TIN
    The TIN data cannot be saved in a geodatabase, so the output data
    should be put into a folder e.g. C:\\ArcGISdata\\chp12data.gdb\\tin
"""
#Please change this file path to your data location
arcpy.ddd.RasterTin("dem", r"F:\GMU\stcenter\repositories\ArcGISdata\chp12data.gdb\tin") 

"""
    TIN to DEM
    The cell size of the new DEM is 50 meters, values are in the 
    float type, and the methos used to raster the DEM is linear
    interpolation 
"""
#Please change this file path to your data location
arcpy.ddd.TinRaster(in_tin=r"F:\GMU\stcenter\repositories\ArcGISdata\chp12data.gdb\tin", out_raster="demFromTIN", \
                   data_type="FLOAT", method="LINEAR", \
                   sample_distance="CELLSIZE 50",z_factor="1")
