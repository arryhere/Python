'''
• Python Tuples
• Tuples are ordered collection of data items
• Tuple items are seperated by commas and enclosed within round brackets ()
• Tuples are immutable (cannot change), we cannot alter them after initialization
'''

tup = (1, 2, 3, 4, 5)
print(tup, type(tup))  # (1, 2, 3, 4, 5) <class 'tup'>

tup = (1)
print(tup, type(tup))  # 1 <class 'int'>

tup = (1,)
print(tup, type(tup))  # (1,) <class 'tuple'>

tup = ()
print(tup, type(tup))  # () <class 'tuple'>


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Indexing in tuples
• tuple[i:j:k]
• i: inclusive, j: exclusive, k: jump
• tuple indexing:
  • ['p', 'y', 't', 'h', 'o', 'n']
  •   0    1    2    3    4    5
  •  -6   -5   -4   -3   -2   -1
'''
tup = ('p', 'y', 't', 'h', 'o', 'n')
print(tup[0])             # p
print(tup[-1])            # n
# tup[0] = 11             # TypeError: 'tuple' object does not support item assignment
print(tup[0:])            # ('p', 'y', 't', 'h', 'o', 'n')
print(tup[:])             # ('p', 'y', 't', 'h', 'o', 'n')
print(tup[:-3])           # ('p', 'y', 't')
print(tup[0:-1:2])        # ('p', 't', 'o')


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• if clause in tuples
'''
tup = (1, True, 'string', [1, 2, 3])

if 1 in tup:
  print('yes, 1 is in tuple')           # yes, 1 is in tuple
else:
  print('no, 1 is not in tuple')

if '1' in tup:
  print('yes, "1" is in tuple')
else:
  print('no, \'1\' is not in tuple')    # no, '1' is not in tuple


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Manipulating Tuples
• Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list
• Then perform operation on that list and convert it back to tuple
'''
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")   # ("Spain", "Italy", "India", "England", "Germany". "Russia")
temp.pop(3)             # "England"
temp[2] = "Finland"     # ("Spain", "Italy", "Finland", "Germany". "Russia")
countries = tuple(temp)
print(countries)        # ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Tuple concatenation
'''
tup1 = (1, 2, 3, 4, 5)
tup2 = ('hello', 'world')

tup3 = tup1 + tup2
print(tup3)  # (1, 2, 3, 4, 5, 'hello', 'world')


print('-----------------------------------------------------------------------------------------------------------------------------------')
