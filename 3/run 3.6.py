a = [1,2,3,4]
print(a)
# Output: [1, 2, 3, 4]
b = [x*3 for x in a]
print(b)
# Output: [3, 6, 9, 12]
print(a[0])
# Output: 1
print(a[3])
# Output: 4
print(len(a))
# Output: 4
print(a[1:3])
# Output: [2, 3]
del a[0]
print(a)
# Output: [2, 3, 4]
print(a*3)
# Output: [2, 3, 4, 2, 3, 4, 2, 3, 4]
print(a+b)
# Output: [2, 3, 4, 3, 6, 9, 12]
a = [1,4,7,9]
sum = 0
for i in a:
    sum+=i

print(sum)
# Output: 21

print(a[4])
# Error Message:
# Traceback (most recent call last):
#   File "<>", line 30, in <module>
#     print(a[4])
# IndexError: list index out of range
