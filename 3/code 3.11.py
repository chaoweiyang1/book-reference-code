>>> s = set(['A','B','C','D'])
>>> t = set(['A','B','E','F'])
>>> s-t
{'C', 'D'}
>>> s&t
{'B', 'A'}
>>> s^t
{'F', 'C', 'D', 'E'}
>>> s|t
{'F', 'C', 'B', 'E', 'D', 'A'}
>>> s.difference(t)
{'C', 'D'}
