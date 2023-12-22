class Test:
    def __init__(self):
        self.__foobar = "private attr"
        self.foobar = "public attr"


test = Test()
print(test.foobar)
# Output: public attr
print(test._Test__foobar)
# Output: private attr
print(test.__foobar)

# Error Message:
# Traceback (most recent call last):
#    File "<>", line 12, in <module>
#    print(test.__foobar)
# AttributeError: 'Test' object has no attribute '__foobar'. Did you mean: 'foobar'?
