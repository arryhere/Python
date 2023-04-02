'''
• Dictionary Methods
• Dictionary uses several built-in methods for data manipulation

• get()
• update()
• clear()
• pop()
• popitem()
• copy()
• setdefault()
• keys()
• values()
• items()
• fromkeys()
'''

'''
• get()
• returns the value of the key
• returns None is key not found
'''
d = {
    'name': 'Arijit',
    'age': 22
}
get = d.get('name')
print(get)  # Arijit


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• update()
• updates the key if already present, else creates a new key
'''
marks = {
    'Science': 99,
    'Maths': 89,
    'Geography': 58,
    'Computer Science': 100
}
new_marks = {
    'History': 67,
    'Maths': 98
}
marks.update(new_marks)
print(marks)  # {'Science': 99, 'Maths': 98, 'Geography': 58, 'Computer Science': 100, 'History': 67}


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• clear()
• removes all the items from the dictionary
'''
d = {
    'name': 'Arijit',
    'age': 22
}
d.clear()
print(d)  # {}


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• pop()
• removes the key-value pair whose key is passed
• returns the popped value
'''
d = {
    'name': 'Arijit',
    'age': 22
}
pop = d.pop('name')
print(pop, d)  # Arijit {'age': 22}


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• popitem()
• removes the last key-value pair from the dictionary
• returns key, value in a tuple
'''
d = {
    'name': 'Arijit',
    'age': 22
}
pop = d.popitem()
print(pop, d)  # ('age', 22) {'name': 'Arijit'}


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• copy()
• creates a shallow copy (1 level deep copy only)
'''

d = {
    'name': 'Arijit',
    'emp': {'name': 'Rahul'}
}
new = d.copy()
print(new)  # {'name': 'Arijit', 'emp': {'name': 'Rahul'}}

d['name'] = 'Sam'
d['emp']['name'] = 'Sam'
print(new)  # {'name': 'Arijit', 'emp': {'name': 'Sam'}}


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• setdefault()
• if only key provided return the value, if key not found return None
• if key-value provided, return the value of key in dict, else create a new key-value if key not present
'''
d = {
    'name': 'Arijit',
    'age': 22
}
v1 = d.setdefault('name', 'Rahul')
v2 = d.setdefault('new_name', 'Rahul')
v3 = d.setdefault('gender')
print(v1)   # Arijit
print(v2)   # Rahul
print(v3)   # None
print(d)    # {'name': 'Arijit', 'age': 22, 'new_name': 'Rahul'}


print('-----------------------------------------------------------------------------------------------------------------------------------')

'''
• keys()
• returns a set-like object providing a view on dict's keys
'''
emp = {
    'firstName': 'Arijit',
    'lastName': 'Das',
    'age': 22,
    'gender': 'Male',
    'alive': True
}
print(emp.keys())  # dict_keys(['firstName', 'lastName', 'age', 'gender', 'alive'])


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• values()
• returns a set-like object providing a view on dict's values
'''
emp = {
    'firstName': 'Arijit',
    'lastName': 'Das',
    'age': 22,
    'gender': 'Male',
    'alive': True
}
print(emp.values())  # dict_values(['Arijit', 'Das', 22, 'Male', True])


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• items()
• returns a set-like object providing a view on dict's items
'''
emp = {
    'firstName': 'Arijit',
    'lastName': 'Das',
    'age': 22,
    'gender': 'Male',
    'alive': True
}
print(emp.items())  # dict_items([('firstName', 'Arijit'), ('lastName', 'Das'), ('age', 22), ('gender', 'Male'), ('alive', True)])


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• fromkeys()
• A dictionary with keys mapped to None if no value is provided, else to the value provided in the field
'''
new = dict.fromkeys((1, 2, 3))
print(new)  # {1: None, 2: None, 3: None}

new = dict.fromkeys((1, 2, 3), 'initial')
print(new)  # {1: 'initial', 2: 'initial', 3: 'initial'}


print('-----------------------------------------------------------------------------------------------------------------------------------')
