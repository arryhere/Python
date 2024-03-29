'''
• Python Lists

• Lists are ordered collection of data items
• They store multiple items in a single variable
• For context its's just like Arrays from other programming languages
• Lists are mutable, we can change them after initialization
'''

nums = [3, 5, 7]
print(nums, type(nums))  # [3, 5, 7] <class 'list'>

ls = []
print(ls, type(ls))  # [] <class 'list'>

print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• indexing in lists
• list[i:j:k]
• i: inclusive, j: exclusive, k: jump
• List indexing:
  • ['p', 'y', 't', 'h', 'o', 'n']
  •   0    1    2    3    4    5
  •  -6   -5   -4   -3   -2   -1
'''
fruits = ['apple', 'banana', 'guave', 'mango', 'pineapple']

print(fruits[0])                        # apple
fruits[0] = 'papaya'
print(fruits)                           # ['papaya', 'banana', 'guave', 'mango', 'pineapple']
print(fruits[0:len(fruits) - 1])        # ['papaya', 'banana', 'guave', 'mango']
print(fruits[0:-1:3])                   # ['papaya', 'mango']


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Iterating a list
'''
pets = ['dog', 'cat', 'fish', 'cow']
for e in pets:
  print(e)  # dog cat fish cow


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• if clause in lists
'''
lst = [2, 3.14, True, 'string', None]
print(lst)                             # [2, 3.14, True, 'string', None]

if 2 in lst:
  print('yes, 2 is present in lst')    # yes, 2 is present in lst
else:
  print('no, 2 is no present in lst')

if '2' in lst:
  print('yes, 2 is present in lst')
else:
  print('no, 2 is no present in lst')  # no, 2 is no present in lst


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• List comprehension
• List comprehension is used to create new lists from other iterables like lists, tuples, dictionaries, sets, and even arrays and strings
• 
'''
lst = [i for i in range(0, 5)]
print(lst)  # [0, 1, 2, 3, 4]

lst = [i*i for i in range(0, 5)]
print(lst)  # [0, 1, 4, 9, 16]

lst = [i for i in range(10) if i % 2 != 0]
print(lst)  # [1, 3, 5, 7, 9]

languages = ['python', 'javascript', 'c', 'c++', 'java', 'carbon']
print([e for e in languages if len(e) <= 1])  # ['c']
print([e for e in languages if 'o' in e])     # ['python', 'carbon']


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• List concatenation
'''

list1 = [1, 2, 3, 4, 5]
list2 = ['hello', 'world']

list3 = list1 + list2
print(list3)  # [1, 2, 3, 4, 5, 'hello', 'world']


print('-----------------------------------------------------------------------------------------------------------------------------------')
