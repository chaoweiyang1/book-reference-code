class Test:
    version = 1.0


print(Test.version)
# Output: 1.0
t1 = Test()
t2 = Test()
print(t1.version)
# Output: 1.0
print(t2.version)
# Output: 1.0
Test.version = 2.0
print(t1.version)
# Output: 2.0
print(t2.version)
# Output: 2.0
t1.version = 3.0
print(t1.version)
# Output: 3.0
print(Test.version)
# Output: 2.0
print(t2.version)
# Output: 2.0
