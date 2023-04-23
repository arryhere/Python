'''
• Class Methods

• Class method is a type of method that is bound to the class and not the instance of the class
• @classmethod decorator -> used to declare class methods
• A class method receives the class as implicit first argument, just like an instance method receives the instance
• 
'''


class Employee:
  company = 'Google'
  domain = 'Software'

  def __init__(self, name):
    self.name = name

  def info(self):
    return {
        "name": self.name,
        "company": self.company,
        "domain": self.domain
    }

  def changeCompany(self, newCompany):
    self.company = newCompany

  @classmethod
  def changeDomain(class_self, newDomain):
    class_self.domain = newDomain


e1 = Employee('Arijit')
print(e1.info())                # {'name': 'Arijit', 'company': 'Google', 'domain': 'Software'}
e1.changeCompany('Microsoft')
e1.changeDomain('Hardware')
print(e1.info())                # {'name': 'Arijit', 'company': 'Microsoft', 'domain': 'Hardware'}

print(Employee.company)         # Google
print(Employee.domain)          # Hardware

e2 = Employee('Divya')
print(e2.info())                # {'name': 'Divya', 'company': 'Google', 'domain': 'Hardware'}


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Class Methods as alternative constructors
• 
'''


class Employee:
  def __init__(self, name: str, salary: int) -> None:
    self.name = name
    self.salary = salary

  @classmethod
  def setClass1(cls, infoString: str, seperator: str):
    ls = infoString.split(seperator)
    return cls(ls[0], int(ls[1]))

  def setClass2(infoString: str, seperator: str):
    ls = infoString.split(seperator)
    return Employee(ls[0], int(ls[1]))

  def info(self):
    return {"name": self.name, "salary": self.salary}


e1 = Employee('Arijit', 1200)
print(e1.info())                              # {'name': 'Arijit', 'salary': 1200}

e2 = Employee.setClass1('Divya-5000', '-')
print(e2.info())                              # {'name': 'Arijit', 'salary': 1200}

e3 = Employee.setClass2('Bhavika-2000', '-')  # can also be done like this
print(e3.info())                              # {'name': 'Arijit', 'salary': 1200}


print('-----------------------------------------------------------------------------------------------------------------------------------')
