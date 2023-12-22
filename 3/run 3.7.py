a = [1,2,3,4]
a.append(10)
print(a)
# Output: [1, 2, 3, 4, 10]
a.insert(2,15)
print(a)
# Output: [1, 2, 15, 3, 4, 10]
print(a.pop())
# Output: 10
print(a)
# Output: [1, 2, 15, 3, 4]
a.sort()
print(a)
# Output: [1, 2, 3, 4, 15]
