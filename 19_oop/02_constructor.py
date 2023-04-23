'''
• Constructors

• Often classes like to create objects with instances customized to a specific initial state, thus may define a special method named __init__()
• When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly created class instance
• __init__() returns None

• Default Constructor
  • the constructor doesn't accept any arguments from the object and has only one argument, self

• Parameterized Constructor
  • the constructor accepts arguments along with self

• Class Variables
  • Class variables are defined at the class level and are shared among all instances of the class
  • They are defined outside of any method and are usually used to store information that is common to all instances of the class

• Instance Variables
  • Instance variables are defined at the instance level and are unique to each instance of the class
  • They are defined inside the init method and are usually used to store information that is specific to each instance of the class
'''


'''
• Default Constructor
'''


class Demo:
  def __init__(self):
    print('Constructor')


a = Demo()                                  # Constructor (called on object creation)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Parameterized Constructor
'''


class Person:
  company = 'Google'                        # class variable (shared by all instances)
  selfCount = 0                             # class variable
  classCount = 0

  def __init__(self, name, age):
    print('Constructor')
    self.name = name                        # instance variable (unique to each instance)
    self.age = age                          # instance variable
    self.sector = 400                       # instance variable
    self.selfCount += 1                     # instance
    Person.classCount += 1                  # class

  def getInfo(self):
    return {
        "name": self.name,
        "age": self.age,
        "sector": self.sector,
        "company": self.company,
        "selfCount": self.selfCount,
        "classCount": self.classCount
    }


a = Person('Arijit', 22,)                   # Constructor (called on object creation)
print(a.getInfo())                          # {'name': 'Arijit', 'age': 22, 'sector': 400, 'company': 'Google', 'selfCount': 1, 'classCount': 1}
a.sector = 200
a.company = 'Microsoft'
a.age = 23
print(a.getInfo())                          # {'name': 'Arijit', 'age': 23, 'sector': 200, 'company': 'Microsoft', 'selfCount': 1, 'classCount': 1}

print(Person.company)                       # Google
Person.company = 'Amazon'

b = Person('Divya', 23)                     # Constructor (called on object creation)
print(b.getInfo())                          # {'name': 'Divya', 'age': 23, 'sector': 400, 'company': 'Amazon', 'selfCount': 1, 'classCount': 2}


print('-----------------------------------------------------------------------------------------------------------------------------------')
