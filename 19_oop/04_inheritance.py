'''
• Inheritance
• Inheritance is when a class is derived from another class
• child-class or sub-class inherit methods and variables from parent-class or base-class
• it allows the programmer to use fewer lines of code, decreasing redundancy and increasing code re-usability

• Types of inheritance
  • Single inheritance
  • Multiple inheritance
  • Multilevel inheritance
  • Hierarchical Inheritance
  • Hybrid Inheritance
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


class Developer(Employee):

  def languages(self):
    return ['JavaScript', 'Python', 'React', 'Nodejs', 'SQL']


emp1 = Employee('Arijit', 23, 'Computer')
print(emp1.employeeInfo())    # {'name': 'Arijit', 'age': 23, 'domain': 'Computer', 'company': 'Microsoft', 'country': 'USA'}

dev1 = Developer('Divya', 22, 'Architecture')
print(dev1.languages())       # ['JavaScript', 'Python', 'React', 'Nodejs', 'SQL']
print(dev1.age)               # 22


print('-----------------------------------------------------------------------------------------------------------------------------------')
