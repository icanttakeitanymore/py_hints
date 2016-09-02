In [66]: def avg_gen(): 
    ...:     total = 0.0
    ...:     count = 0
    ...:     average = None
    ...:     while True:
    ...:         term = yield average
    ...:         total += term
    ...:         count += 1
    ...:         average = total/count
  
in [48]: avg = avg_gen()

In [49]: next(avg)

In [50]: avg.send(10)
Out[50]: 10.0

In [51]: avg.send(10)
Out[51]: 10.0

In [52]: avg.send(10)
Out[52]: 10.0

In [53]: avg.send(10)
Out[53]: 10.0

In [54]: avg.send(10)
Out[54]: 10.0

In [55]: 

In [55]: avg.send(20)
Out[55]: 11.666666666666666
