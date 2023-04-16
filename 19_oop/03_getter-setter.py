'''
• Getters & Setters

• 
• 
'''


class Employee:
  company = 'Microsoft'
  country = 'USA'

  def __init__(self, name, age, domain):
    self.name = name
    self.age = age
    self.domain = domain

  def employeeInfo(self):
    return {
        "name": self.name,
        "age": self.age,
        "domain": self.domain,
        "company": self.company,
        "country": self.country
    }

  @property
  def __age__(self):
    return self.age

  @__age__.setter
  def __age__(self, newAge):
    self.age = newAge


emp = Employee('Arijit', 23, 'Computer')

print(emp.employeeInfo())  # {'name': 'Arijit', 'age': 23, 'domain': 'Computer', 'company': 'Microsoft', 'country': 'USA'}
print(emp.__age__)         # 23
emp.__age__ = 55
print(emp.__age__)         # 55


print('-----------------------------------------------------------------------------------------------------------------------------------')
