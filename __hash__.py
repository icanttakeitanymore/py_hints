In [151]: class Vector2d:
     ...:     typecode = 'd'
     ...:     def __init__(self, x, y):
     ...:         self.__x = float(x)
     ...:         self.__y = float(y)
     ...:     @property
     ...:     def x(self):
     ...:         return self.__x
     ...:     @property
     ...:     def y(self):
     ...:         return self.__y
     ...:     def __repr__(self):
     ...:         return "Vector2d({x},{y})".format(x=self.x,y=self.y)
     ...:     def __add__(self, right):
     ...:         return Vector2d(self.x + right.x,self.y + right.y)
     ...:     def __iter__(self):
     ...:         return (i for i in (self.x, self.y))
     ...:     def __eq__(self, another):
     ...:         if self.x == another.x and self.y == another.y:
     ...:             return True
     ...:         else:
     ...:             return False
     ...:     def __format__(self, format_spec=''):
     ...:         components = (format(c, format_spec) for c in self)
     ...:         return 'Vector2d({},{})'.format(*components)
     ...:     def __hash__(self):
     ...:         return hash(self.x) ^ hash(self.y)
     
     
In [158]: v6 = Vector2d(10,5)

In [159]: v6.__hash__()
Out[159]: 15

In [160]: v7 = Vector2d(10.1,5.9)

In [161]: v7.__hash__()
Out[161]: 2305843009213685775

In [162]: set([v6,v7])
Out[162]: {Vector2d(10.1,5.9), Vector2d(10.0,5.0)}
