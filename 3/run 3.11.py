s = set(['A','B','C','D'])
t = set(['A','B','E','F'])
print(s-t)
# Output: {'D', 'C'}
print(s&t)
# Output: {'A', 'B'}
print(s^t)
# Output: {'E', 'C', 'D', 'F'}
print(s|t)
# Output: {'E', 'C', 'B', 'D', 'F', 'A'}
print(s.difference(t))
# Output: {'D', 'C'}
