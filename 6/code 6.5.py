>>> import struct
>>> f = open(r'F:\GMU\stcenter\repositories\book-reference-code\6\data\Schools.shp','rb') # Change path as needed
>>> s = f.read(28)
>>> b = struct.unpack('>iiiiiii',s)
>>> print(b)
(9994, 0, 0, 0, 0, 0, 288)
>>> s = f.read(72)
>>> b = struct.unpack('<iidddddddd',s)

>>> print(b)
(1000, 1, 1847318.8628035933,
 765532.64196603, 1859639.8841250539, 778092.9935274571, 0.0, 0.0, 0.0, 0.0)
