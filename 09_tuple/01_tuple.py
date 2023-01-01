'''
• Python Tuples
• Tuples are ordered collection of data items
• Tuple items are seperated by commas and enclosed within round brackets ()
• Tuples are immutable (cannot change), we cannot alter them after initialization
'''

tuple = (1, 2, 3, 4, 5)
print(tuple, type(tuple))  # (1, 2, 3, 4, 5) <class 'tuple'>

tuple = (1)
print(tuple, type(tuple))  # 1 <class 'int'>

tuple = (1,)
print(tuple, type(tuple))  # (1,) <class 'tuple'>


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• Indexing in tuples
• tuple[i:j:k]
• i: inclusive, j: exclusive, k: jump
• tuple indexing:
  • ['p', 'y', 't', 'h', 'o', 'n']
  •   0    1    2    3    4    5
  •  -6   -5   -4   -3   -2   -1
'''
tuple = ('p', 'y', 't', 'h', 'o', 'n')
print(tuple[0])             # p
print(tuple[-1])            # n
# tuple[0] = 11             # TypeError: 'tuple' object does not support item assignment
print(tuple[0:])            # ('p', 'y', 't', 'h', 'o', 'n')
print(tuple[:])             # ('p', 'y', 't', 'h', 'o', 'n')
print(tuple[:-3])           # ('p', 'y', 't')
print(tuple[0:-1:2])        # ('p', 't', 'o')


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• if clause in tuples
'''
tuple = (1, True, 'string', [1, 2, 3])

if 1 in tuple:
  print('yes, 1 is in tuple')       # yes, 1 is in tuple
else:
  print('no, 1 is not in tuple')

if '1' in tuple:
  print('yes, "1" is in tuple')
else:
  print('no, \'1\' is not in tuple')    # no, '1' is not in tuple


print('-------------------------------------------------------------------------------------------------------------------------')
