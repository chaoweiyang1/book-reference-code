import struct

x,y,z = 100, 200, 300
s = struct.pack('<iii',x,y,z)

print(s)

s = struct.pack('iii',x,y,z)
print(s)