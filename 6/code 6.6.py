>>> import struct
>>> f = open(r'F:\GMU\stcenter\repositories\book-reference-code\6\data\Schools.shp','rb') # Change path as needed
>>> f.seek(24)
>>> s = f.read(4)
>>> b = struct.unpack('>i',s)
>>> featNum = (b[0]*2-100)/28
>>> out = open(r'F:\GMU\stcenter\repositories\book-reference-code\6\data\schools_shp.txt','w') # Change path as needed
>>> for i in range(int(featNum)):
        f.seek(100+i*28+12)
        s = f.read(16)
        x,y = struct.unpack('dd',s)
        out.write(str(i)+':'+str(x)+','+str(y)+'\n')
>>> f.close()
>>> out.close()
