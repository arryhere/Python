'''
• Dunder methods

• They're special methods that you can define to add "magic" to your classes
• They're always surrounded by double underscores (e.g. __init__ or __lt__)
• They are incredibly powerful tools that allow you to customize the behaviour of your objects, and can make your code much cleaner and easier to understand
• 
'''


class Vector:
  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y

  def __del__(self):
    print(f"{self} is destroyed")       # <__main__.Person object at 0x00000293E3C8EF10> is destroyed

  def __repr__(self):
    return f"({self.x}, {self.y})"

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __mul__(self, other):
    return Vector(self.x * other.x, self.y * other.y)

  def __len__(self):
    return 2

  def __call__(self):
    print(f"{self} is called")


v1 = Vector(44, 23)
v2 = Vector(2, 7)

v3 = v1 + v2                          # __add__ is working here
print(v3)                             # (46 30)
print(len(v3))                        # __len__ is working here | 2

v4 = v1 * v2                          # __mul__ is working here
print(v4)                             # (88, 161)
v4()                                  # (88, 161) is called


'''
(44, 23) is destroyed
(2, 7) is destroyed
(46, 30) is destroyed
(88, 161) is destroyed
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://stackoverflow.com/questions/1418825/where-is-the-python-documentation-for-the-special-methods-init-new
• https://rszalski.github.io/magicmethods/

• __abs__
• __abstractmethods__
• __add__
• __alloc__
• __and__
• __annotations__
• __base__
• __bases__
• __basicsize__
• __bool__
• __builtins__
• __cached__
• __call__
• __ceil__
• __class__
• __class_getitem__
• __contains__
• __delattr__
• __delitem__
• __dict__
• __dictoffset__
• __dir__
• __divmod__
• __doc__
• __enter__
• __eq__
• __exit__
• __file__
• __flags__
• __float__
• __floor__
• __floordiv__
• __format__
• __ge__
• __getattribute__
• __getformat__
• __getitem__
• __getnewargs__
• __gt__
• __hash__
• __iadd__
• __iand__
• __imul__
• __index__
• __init__
• __init_subclass__
• __instancecheck__
• __int__
• __invert__
• __ior__
• __isub__
• __itemsize__
• __iter__
• __ixor__
• __le__
• __len__
• __loader__
• __lshift__
• __lt__
• __mod__
• __module__
• __mro__
• __mul__
• __name__
• __ne__
• __neg__
• __new__
• __or__
• __package__
• __pos__
• __pow__
• __prepare__
• __qualname__
• __radd__
• __rand__
• __rdivmod__
• __reduce__
• __reduce_ex__
• __repr__
• __reversed__
• __rfloordiv__
• __rlshift__
• __rmod__
• __rmul__
• __ror__
• __round__
• __rpow__
• __rrshift__
• __rshift__
• __rsub__
• __rtruediv__
• __rxor__
• __set_format__
• __setattr__
• __setitem__
• __sizeof__
• __slots__
• __spec__
• __str__
• __sub__
• __subclasscheck__
• __subclasses__
• __subclasshook__
• __text_signature__
• __truediv__
• __trunc__
• __weakrefoffset__
• __xor__
'''
