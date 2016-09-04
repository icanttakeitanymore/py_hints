In [8]: def coroutine(func):
   ...:     @wraps(func)
   ...:     def primer(*args, **kwargs):
   ...:         gen = func(*args, **kwargs)
   ...:         next(gen)
   ...:         return gen
   ...:     return primer
   ...: 

In [9]: @coroutine
   ...: def averenger():
   ...:     total = 0.0
   ...:     counter = 0
   ...:     avg = None
   ...:     while True:
   ...:         counter += 1
   ...:         x = yield avg
   ...:         total += x
   ...:         avg = total / counter
   ...:         

