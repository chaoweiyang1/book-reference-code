>>> import struct
>>> f = open(r'F:\GMU\stcenter\repositories\book-reference-code\6\data\Schools.shx','rb') # Change path as needed
>>> f.seek(24)
>>> s = f.read(4)
>>> b = struct.unpack('>i',s)
>>> featNum = (b[0]*2-100)/8
>>> out = open(r'F:\GMU\stcenter\repositories\book-reference-code\6\data\schools_index.txt','w') # Change path as needed
>>> for i in range(int(featNum)):
        f.seek(100+i*8)
        s = f.read(8)
        off,length = struct.unpack('>ii',s)
        out.write(str(i)+':'+str(off)+','+str(length)+'\n')
>>> f.close()
>>> out.close()
