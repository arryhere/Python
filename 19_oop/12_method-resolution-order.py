'''
• Method Resolution Order - MRO

• super == next in line
• in single inheritance , next in line in parent
• super(__class__, self)
  • __class__ : class that its currently being run from
  • self      : object that its currently being run on
• 
'''


class Root:
  f = 'Root'


class A(Root):
  f = 'A'


class B(Root):
  f = 'B'


class C(A, B):
  f = 'C'


c = C()
print(c.f)      # C


print('-----------------------------------------------------------------------------------------------------------------------------------')


class Root:
  f = 'Root'


class A(Root):
  f = 'A'


class B(Root):
  f = 'B'


class C(A, B):
  pass


c = C()
print(c.f)      # A


print('-----------------------------------------------------------------------------------------------------------------------------------')


class Root:
  f = 'Root'


class A(Root):
  pass


class B(Root):
  f = 'B'


class C(A, B):
  pass


c = C()
print(c.f)      # B


print('-----------------------------------------------------------------------------------------------------------------------------------')


class Root:     # (Root, object)
  f = 'Root'


class A(Root):  # (A, object)
  pass


class B(Root):  # (B, object)
  pass


class C(A, B):  # C < A < B < object
  pass


c = C()
print(c.f)      # Root

print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Root'>, <class 'object'>]


print('###################################################################################################################################')


class Root1:
  def __init__(self) -> None:
    print('Root 1')


class Root2:
  def __init__(self) -> None:
    print('Root 2')


class Child(Root1, Root2):
  def __init__(self) -> None:
    print('Child')
    super(Child, self).__init__()
    super(Root1, self).__init__()
    super(Root2, self).__init__()


c = Child()
'''
Child
Root 1
Root 2
'''


print('###################################################################################################################################')
