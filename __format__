```
In [108]: class Vector2d:
     ...:     def __init__(self, x, y):
     ...:         self._x = x
     ...:         self._y = y
     ...:     def __repr__(self):
     ...:         return "Vector2d({_x},{_y})".format(_x=self._x,_y=self._y)
     ...:     def __add__(self, right):
     ...:         return Vector2d(self._x + right._x,self._y + right._y)
     ...:     def __iter__(self):
     ...:         return (i for i in (self._x, self._y))
     ...:     def __format__(self, format_spec=''):
     ...:         components = (format(c, format_spec) for c in self)
     ...:         return 'Vector2d({},{})'.format(*components)


In [109]: v1 = Vector2d(3,4)
In [114]: format(v1, 'f')
Out[114]: 'Vector2d(3.000000,4.000000)'

In [115]: format(v1, '0.5f')
Out[115]: 'Vector2d(3.00000,4.00000)'

In [116]: format(v1, '0.3f')
Out[116]: 'Vector2d(3.000,4.000)'

In [117]: format(v1, '0.2f')
Out[117]: 'Vector2d(3.00,4.00)'

```
