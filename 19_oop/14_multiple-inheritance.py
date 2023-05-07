'''
• Multiple Inheritance

• It allows a class to inherit attributes and methods from multiple parent classes
• 
'''


class Base1:
  def __init__(self, prop1) -> None:
    print('Class Base1')
    self.prop1 = prop1

  def show(self):
    print(f"I am Base1")


class Base2:
  def __init__(self, prop2) -> None:
    print('Class Base2')
    self.prop2 = prop2

  def show(self):
    print(f"I am Base2")


class Child(Base1, Base2):
  def __init__(self, prop1, prop2) -> None:
    super().__init__(prop1)
    Base2.__init__(self, prop2)
    super(Base1, self).__init__(prop2)    # same as -> Base2.__init__(self, prop2)


child = Child('Base1 prop 1', 'Base1 prop 2')
'''
Class Base1
Class Base2
'''
child.show()        # I am Base1

print(Child.mro())  # [<class '__main__.Child'>, <class '__main__.Base1'>, <class '__main__.Base2'>, <class 'object'>]
print(Base2.mro())
print(Base1.mro())