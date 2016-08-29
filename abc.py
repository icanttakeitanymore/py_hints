In [14]: class Tombola(abc.ABC):
    ...:     @abc.abstractmethod
    ...:     def load(self,iterable):
    ...:         """
    ...:         Добавить элементы из итерируемого объекта
    ...:         """
    ...:     @abc.abstractmethod
    ...:     def pick(self):
    ...:         """
    ...:         извлечь случайный элемент и вернуть его
    ...:         Этот метот должен возбудать исключение `loo
    ...: kuperror`,
    ...:         если объект пуст.
    ...:         """
    ...:     def loaded(self):
    ...:         """
    ...:         вернуть True, если хотя один элемент есть, 
    ...: иначе False"""
    ...:         return bool(self.inspect())
    ...:     def inspect(self):
    ...:         """
    ...:         вернуть отсортированный кортеж содержащий н
    ...: аходящиеся в
    ...:         контейнере элементы
    ...:         """
    ...:         items = []
    ...:         while True:
    ...:             try:
    ...:                 items.append(self.pick())
    ...:             except LookupError:
    ...:                 break
    ...:         self.load(items)
    ...:         return tuple(sorted(items))
    
    
    
    
    In [18]: class BingoCage(Tombola):
    ...:     def __init__(self, items):
    ...:         self._randomizer = random.SystemRandom()
    ...:         self._items = []
    ...:         self.load(items)
    ...:     def load(self, items):
    ...:         self._items.extend(items)
    ...:         self._randomizer.shuffle(self._items)
    ...:     def pick(self):
    ...:         try:
    ...:             return self._items.pop()
    ...:         except IndexError:
    ...:             raise LookupError('pick from empty Bing
    ...: oCage')
    ...:     def __call__(self):
    ...:         self.pick()
