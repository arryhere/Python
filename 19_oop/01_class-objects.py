'''
• Class
  • classes provide a means of bundling data and functionality together, a blueprint or a template for creating objects
  • creating a new class creates a new type of object, allowing new instances of that type to be made
  • each class instance can have attributes attached to it for maintaining its state
  • class instances can also have methods (defined by its class) for modifying its state
  • 

• Object
  • object is the instance of a class
  • used to access the properties and methods of a class
  • 

• self keyword
  • self parameter is a reference to the current instance of the class (current object)
  • it is used to access properties that belongs to the class of which the instance is created
'''


class Person:       # class
  name = 'Arijit'
  age = 22
  role = 'Dev Ops'

  def getInfo(self):
    return f"name: {self.name}, age: {self.age}, role: {self.role}"


a = Person()        # object

print(a.name)       # Arijit
print(a.age)        # 22
print(a.role)       # Dev Ops
print(a.getInfo())  # name: Arijit, age: 22, role: Dev Ops

a.name = 'Rahul'
a.age = 24
a.role = 'Architecture'

print(a.name)       # Rahul
print(a.age)        # 24
print(a.role)       # Architecture
print(a.getInfo())  # name: Rahul, age: 24, role: Architecture


print('-----------------------------------------------------------------------------------------------------------------------------------')

