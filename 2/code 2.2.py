>>> class Test:
	def __init__(self):
		self.__foobar = "private attr"
		self.foobar = "public attr"

		
>>> test = Test()
>>> test.foobar
'public attr'
>>> test.__foobar

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    test.__foobar
AttributeError: 'Test' object has no attribute '__foobar'. Did you mean: 'foobar'?
>>> test._Test__foobar
'private attr'
>>> 
