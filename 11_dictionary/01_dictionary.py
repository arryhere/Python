'''
• Python Dictionaries

• Dictionaries are ordered collection of data items
• Dictionary items are 'key-value' pairs that are seperated by comma and enclosed within curly braces
'''

d = {
    'name': 'Arijit',
    'age': 22,
    'isAlive': True,
    'isAlive': True,  # repeating key
}

print(d, type(d))     # {'name': 'Arijit', 'age': 22, 'isAlive': True} <class 'dict'>

d['name'] = 'Rahul'
print(d['name'])      # Rahul
print(d['age'])       # 22
print(d['isAlive'])   # True

print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• keys()
• Iterating keys in Dictionary
'''


employee = {
    'firstName': 'Arijit',
    'lastName': 'Das',
    'age': 22,
    'gender': 'Male',
    'alive': True
}

print(employee.keys())  # dict_keys(['firstName', 'lastName', 'age', 'gender', 'alive'])

for key in employee.keys():
  print(f"{key} -> {employee[key]}")

# firstName -> Arijit
# lastName -> Das
# age -> 22
# gender -> Male
# alive -> True


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• values()
• Iterating values in Dictionary
'''

employee = {
    'firstName': 'Arijit',
    'lastName': 'Das',
    'age': 22,
    'gender': 'Male',
    'alive': True
}

print(employee.values())  # dict_values(['Arijit', 'Das', 22, 'Male', True])

for value in employee.values():
  print(value)

# Arijit
# Das
# 22
# Male
# True


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• items()
'''

employee = {
    'firstName': 'Arijit',
    'lastName': 'Das',
    'age': 22,
}

print(employee.items())  # dict_items([('firstName', 'Arijit'), ('lastName', 'Das'), ('age', 22)])

for (x, y) in employee.items():
  print(f"{x} -> {y}")

# firstName -> Arijit
# lastName -> Das
# age -> 22


print('-----------------------------------------------------------------------------------------------------------------------------------')
