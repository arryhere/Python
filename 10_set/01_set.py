'''
• Python Sets
• Sets are unordered collection of data items
• They store multiple ites in a single variable
• Set items are seperated by commas and enclosed within curly brackets {}
• Sets are immutable , and do not contain duplicate items
'''

s = {2, 4, 6, 2}
print(s, type(s))  # {2, 4, 6} <class 'set'>

s = {True, 'python', 33, 3.3}
print(s)  # {True, 3.3, 33, 'python'} or {True, 'python', 3.3, 33} or {'python', True, 3.3, 33} or ... unordered collection

s = {}
print(s, type(s))  # {} <class 'dict'>
s = set()
print(s, type(s))  # set() <class 'set'>


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Iterating sets
'''
s = {True, 'python', 33, 3.3, 'python', False, True}
for e in s:
  print(e)  # False True 33 3.3 python


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• if clause in sets
'''
s = {True, 'python', 33, 3.3, 'python', False, True}

if 'python' in s:
  print('Yes')
else:
  print('No')


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Set comprehension
• Set comprehension is used to create new sets from other iterables
• 
'''
s = {i for i in range(0, 5)}
print(s)  # {0, 1, 2, 3, 4}

s = {i*i for i in range(0, 5)}
print(s)  # {0, 1, 4, 9, 16}

s = {i for i in range(10) if i % 2 != 0}
print(s)  # {1, 3, 5, 7, 9}

languages = ['python', 'javascript', 'c', 'c++', 'java', 'carbon']
print({e for e in languages if len(e) <= 1})  # {'c'}
print({e for e in languages if 'o' in e})     # {'python', 'carbon'}


print('-----------------------------------------------------------------------------------------------------------------------------------')
