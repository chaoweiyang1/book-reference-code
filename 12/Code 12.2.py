import arcpy
from arcpy.sa import *

"""
    The input is "dem" and the output is "contour".
    The contour is in 10 meter intervals and starts from 330 meters.
"""
#Please change this file path to your data location
arcpy.env.workspace = r"F:\GMU\stcenter\repositories\ArcGISdata\chp12data.gdb"

Contour(in_raster="dem", out_polyline_features=" contour", \
                 contour_interval="10", base_contour="330", z_factor="1")