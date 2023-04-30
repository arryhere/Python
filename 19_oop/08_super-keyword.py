'''
• super()

• The super() keyword in Python is used to refer to the parent class
• It is useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes

• When a class inherits from a parent class, it can override or extend the methods defined in the parent class
• However, sometimes you might want to use the parent class method in the child class
• This is where the super() keyword comes in handy
• 
• 
'''


class Base:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def baseInfo(self):
    print({"name": self.name, "age": self.age})


class Child(Base):
  def __init__(self, name, age, domain) -> None:
    super().__init__(name, age)
    self.domain = domain

  def childInfo(self):
    print({"name": self.name, "age": self.age, "domain": self.domain})
    super().baseInfo()


obj_1 = Child('Suku', 23, 'Computer')
obj_1.baseInfo()                    # {'name': 'Suku', 'age': 23}
obj_1.childInfo()                   # {'name': 'Suku', 'age': 23, 'domain': 'Computer'} {'name': 'Suku', 'age': 23}


print('-----------------------------------------------------------------------------------------------------------------------------------')


class A:
  def __init__(self) -> None:
    print('class A')


class B(A):
  def __init__(self) -> None:
    print('class B')
    A.__init__(self)                # not using super, but it does the exact same thing


obj = B()                           # class B class A


class A:
  def __init__(self) -> None:
    print('class A')


class B(A):
  def __init__(self) -> None:
    print('class B')
    super().__init__()
    # super('A', self).__init__()   # same as above, thus not required to use this syntax, nice and clean


obj = B()                           # class B class A


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Diamond shaped inheritance

•     A
    /  \
   B    C
   \   /
     D
'''


class A:
  def __init__(self) -> None:
    print('class A')


class B(A):
  def __init__(self) -> None:
    print('class B')
    A.__init__(self)


class C(A):
  def __init__(self) -> None:
    print('class C')
    A.__init__(self)


class D(B, C):
  def __init__(self) -> None:
    print('class D')
    B.__init__(self)
    C.__init__(self)


obj = D()
'''
class D
class B
class A
class C
class A
'''


class A:
  def __init__(self) -> None:
    print('class A')


class B(A):
  def __init__(self) -> None:
    print('class B')
    super().__init__()


class C(A):
  def __init__(self) -> None:
    print('class C')
    super().__init__()


class D(B, C):
  def __init__(self) -> None:
    print('class D')
    super().__init__()


obj = D()
'''
class D
class B
class C
class A
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://www.youtube.com/watch?v=zS0HyfN7Pm4
• 
'''