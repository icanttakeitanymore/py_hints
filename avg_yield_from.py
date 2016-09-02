In [109]: def main(data):
     ...:     results = {}
     ...:     for key,values in data.items():
     ...:         group = grouper(results, key)
     ...:         next(group)
     ...:         for value in values:
     ...:             group.send(value)
     ...:         group.send(None)
     ...:         

In [110]: def main(data):
     ...:     results = {}
     ...:     for key,values in data.items():
     ...:         group = grouper(results, key)
     ...:         next(group)
     ...:         for value in values:
     ...:             group.send(value)
     ...:         group.send(None)
     ...:         print(results)
     ...:         

In [111]: def main(data):
     ...:     results = {}
     ...:     for key,values in data.items():
     ...:         group = grouper(results, key)
     ...:         next(group)
     ...:         for value in values:
     ...:             group.send(value)
     ...:         group.send(None)
     ...:         #print(results)
     ...:         report(results)
     ...:         

In [112]: def report(results):
     ...:     for key, result in sorted(results.items()):
     ...:         group, unit = key.split(';')
     ...:         print('{:2} {:5} averaging {:.2f}{}'.format(
     ...:         result.count, group, result.average, unit))
     ...:         

In [113]: main({'girls;kg':[50,60,70]})
 3 girls averaging 60.00kg

In [114]: main({'speed;mbit/s':[50,60,70]})
 3 speed averaging 60.00mbit/s

In [115]: main({'speed;mbit/s':[50,60,70,100]})
 4 speed averaging 70.00mbit/s

In [116]: main({'speed;mbit/s':[50,60,70,100,150]})
 5 speed averaging 86.00mbit/s

In [117]: main({'speed;mbit/s':[50,60,70,100,150,400]})
 6 speed averaging 138.33mbit/s
