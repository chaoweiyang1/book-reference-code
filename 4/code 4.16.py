>>> f = open (r'C:\Users\Phil\points.txt', 'r') # Modify path as needed
>>> f.readline()  # Read the 1st  line
'point:\n'
>>> f.readline() # Read the 2nd line
'p1: 1.0, 1.0 \n'
>>> f.readline()  # Read the 3rd line
'p2: 2.0, 2.0 \n'
>>> f.readline() # end of the file
''
>>> f.seek(0)  #go to the begin of file
0
>>> f.readline()
'point:\n' 
>>> f.readlines() # read rest lines in a list
['p1: 1.0, 1.0 \n', 'p2: 2.0, 2.0 \n']
>>> f.seek(0)
0
>>> f.read() # read rest lines as a string
'point:\np1: 1.0, 1.0 \np2: 2.0, 2.0 \n'
>>> f.close()
