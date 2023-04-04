'''
• Constructors
• often classes like to create objects with instances customized to a specific initial state, thus may define a special method named __init__()
• when a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly created class instance
• __init__() returns None
'''

'''
• Default Constructor
• the constructor doesn't accept any arguments from the object and has only one argument, self
'''


class Demo:
  def __init__(self):
    print('Constructor')


a = Demo()                                  # Constructor (called on object creation)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Parameterized Constructor
• the constructor accepts arguments along with self
'''


class Person:
  company = 'Google'                        # class variable shared by all instances

  def __init__(self, name, age, role):
    print('Constructor')
    self.name = name                        # instance variable unique to each instance
    self.age = age                          # instance variable
    self.role = role                        # instance variable

  def getInfo(self):
    return f"name: {self.name}, age: {self.age}, role: {self.role}, company: {self.company}"


a = Person('Arijit', 22, 'Dev Ops')         # Constructor (called on object creation)
print(a.getInfo())                          # name: Arijit, age: 22, role: Dev Ops, company: Google

b = Person('Divya', 23, 'Architecture')     # Constructor (called on object creation)
print(b.getInfo())                          # name: Divya, age: 23, role: Architecture, company: Google


print('-----------------------------------------------------------------------------------------------------------------------------------')
