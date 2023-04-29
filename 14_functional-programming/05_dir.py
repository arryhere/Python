'''
• dir()

• arguments: dir(object)
• Without arguments: return the list of names in the current local scope
• With an argument: attempt to return a list of valid attributes for that object
• 
'''


print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


ls = [1, 2, 3, 4, 'python']
print(dir(ls))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://docs.python.org/3/library/functions.html#dir
• 
'''
