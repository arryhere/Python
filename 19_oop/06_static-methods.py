'''
• Static Methods

• Static methods in python are methods that belong to class, rather than an instance of a class
• A static method does not receive an implicit first argument
• @staticmethod decorator -> used to declare static methods
• static methods do not have access to the instance of the class i.e self
• Use case -> create utility functions that do not need access to instance data
• 
'''

from functools import reduce


class Math:
  def __init__(self):
    pass

  def add(self, *args: int) -> int:
    return reduce(lambda x, y: x + y, args)

  @staticmethod
  def mul(*args: int) -> int:
    return reduce(lambda x, y: x * y, args)


obj = Math()

print(obj.add(2, 2, 2))         # 6
print(Math.add(obj, 2, 2, 2))   # 6

print(obj.mul(2, 2, 2))         # 8
print(Math.mul(2, 2, 2))        # 8


print('-----------------------------------------------------------------------------------------------------------------------------------')
