In [132]: def unpacker(data):
     ...:     while any([isinstance(x,Iterable) and isinstance(x,Sequence)  and len(x) > 1 for x in data]):
     ...:             data = list(worker(data))
     ...:     return data
     ...:     
     ...: 

In [133]: def worker(data):
     ...:     for i in data:
     ...:         if isinstance(i, Iterable) and isinstance(i, Sequence) and len(i) > 1:
     ...:            yield from i
     ...:         else:
     ...:            yield i
     ...:            

In [134]: sequence
Out[134]: 
[1,
 2,
 3,
 [4, [5, 6]],
 (7, 8, 9),
 {10, 11},
 ['sequence1', 'sequence2'],
 {'e': 1}]

In [135]: unpacker(sequence)
Out[135]: 
[1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 {10, 11},
 's',
 'e',
 'q',
 'u',
 'e',
 'n',
 'c',
 'e',
 '1',
 's',
 'e',
 'q',
 'u',
 'e',
 'n',
 'c',
 'e',
 '2',
 {'e': 1}]

In [136]: 
