a = [1,2,3,4]
print(a)
# Output: [1, 2, 3, 4]
a[0]=5
print(a)
# Output: [5, 2, 3, 4]
x = (1,2,3,4)
print(x)
# Output: (1, 2, 3, 4)
x[0]=5

# Error Message:
# Traceback (most recent call last):
#   File "<>", line 10, in <module>
#     x[0]=5
# TypeError: 'tuple' object does not support item assignment
