'''
• Single Inheritance

• Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class
• This is the simplest and most common form of inheritance
• 
'''


class Country:
  def __init__(self, countryName: str) -> None:
    self.countryName = countryName

  def info(self):
    return {"countryName": self.countryName}


class State(Country):
  def __init__(self, countryName: str, stateName: str) -> None:
    super().__init__(countryName)
    self.stateName = stateName

  def info(self):
    return {"countryName": self.countryName, "stateName": self.stateName}


india = Country("India")

mumbai = State("India", "Mumbai")


print(india.info())     # {'countryName': 'India'}
print(mumbai.info())    # {'countryName': 'India', 'stateName': 'Mumbai'}


print('-----------------------------------------------------------------------------------------------------------------------------------')
