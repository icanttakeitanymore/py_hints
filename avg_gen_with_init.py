In [87]: def coroutine(func):
    ...:     @wraps(func)
    ...:     def primer(*args, **kwargs):
    ...:         gen = func(*args, **kwargs)
    ...:         next(gen)
    ...:         return gen
    ...:     return primer
    ...: 

In [88]: @coroutine
    ...: def avg_gen():
    ...:     total = 0.0
    ...:     count = 0
    ...:     average = None
    ...:     while True:
    ...:         term = yield average
    ...:         total += term
    ...:         count += 1
    ...:         average = total/count
    ...:         

In [89]: coro_avg = avg_gen()

In [90]: coro_avg(10)
