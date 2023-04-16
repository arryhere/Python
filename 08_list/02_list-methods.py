'''
• List Methods

• 
• 
• 
• 
'''


'''
• list indexing
• list[i:j:k]
• i: inclusive j: exclusive, k: jump
• List indexing:
  • ['p', 'y', 't', 'h', 'o', 'n']
  •   0    1    2    3    4    5
  •  -6   -5   -4   -3   -2   -1
'''
lst = ['p', 'y', 't', 'h', 'o', 'n']

print(lst[0])                   # p
print(lst[0:])                  # ['p', 'y', 't', 'h', 'o', 'n']
print(lst[:])                   # ['p', 'y', 't', 'h', 'o', 'n']
print(lst[:3])                  # ['p', 'y', 't']
print(lst[:-3])                 # ['p', 'y', 't']
print(lst[0: len(lst)])         # ['p', 'y', 't', 'h', 'o', 'n']
print(lst[0:-1])                # ['p', 'y', 't', 'h', 'o']
print(lst[0: len(lst) - 1])     # ['p', 'y', 't', 'h', 'o']
print(lst[2:5])                 # ['t', 'h', 'o']
print(lst[-4:-1])               # ['t', 'h', 'o']
print(lst[0:len(lst):3])        # ['p', 'h']
print(lst[0::3])                # ['p', 'h']


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• append()
• add object at end of list
• mutates the original list
'''
lst = [1, 2, 3, 4, 5]
lst.append(55)
print(lst)  # [1, 2, 3, 4, 5, 55]


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• sort()
• sorts the list in ascending order by default
• parameters: reverse, key
• reverse: (Optional), default is reverse=False, reverse=True will sort the list in descending order
• key: (Optional), A function to specify the sorting criteria(s)
• mutates the original list
'''

lst = [44, 56, 2, 576, 2, 6]
lst.sort()
print(lst)  # [2, 2, 6, 44, 56, 576]

lst.sort(reverse=True)
print(lst)  # [576, 56, 44, 6, 2, 2]

fruits = ['banana', 'apple', 'mango', 'guava']
fruits.sort()
print(fruits)  # ['apple', 'banana', 'guava', 'mango']


def getLastElement(str):
  return str[-1]


fruits.sort(key=getLastElement)
print(fruits)  # ['banana', 'guava', 'apple', 'mango']


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• reverse()
• reverse the order of the list
• mutates the original list
'''
lst = [1, '2', [True, False], None, 'python', {'age': 22}]
lst.reverse()
print(lst)  # [None, [True, False], '2', 1]


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• index()
• parameters: value, start_index(inclusive), end_index(excusive)
• returns the index of the first occurance of the item in the list
• throws error if item not in list
'''
lst = [1, 2, 3, 4, 5, 3, 3, 6, 3]
# print(lst.index('2'))              # ValueError: 2 is not in lst
print(lst.index(3))                  # 2
print(lst.index(3, 4, -1))           # 5


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• count()
• returns the count of the number of items present in the list
'''

lst = [1, 2, 3, 4, 1, 1, 3, 4]
print(lst.count(1))    # 3
print(lst.count(4))    # 2
print(lst.count(44))   # 0


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• copy()
• returns a copy of the list
• does not modify the original list
'''
list_1 = [1, 2, 3, 4, 5]

newList_1 = list_1
newList_1[0] = 5

print(list_1)                     # [5, 2, 3, 4, 5] -> original list changed as they both have the same reference in memory
print(newList_1)                  # [5, 2, 3, 4, 5]
print(id(list_1), id(newList_1))  # 1971795192896 1971795192896 -> same id, same reference in memory

list_2 = [1, 2, 3, 4, 5]

newList_2 = list_2.copy()
newList_2[0] = 5

print(list_2)                     # [1, 2, 3, 4, 5] -> original list does not change as they have different references in memory
print(newList_2)                  # [5, 2, 3, 4, 5]
print(id(list_2), id(newList_2))  # 1971793265664 1971795257728 -> different id, different reference in memory


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• insert()
• inserts an item at the given index
• mutates the original list
'''
lst = [1, 2, 3, 4, 5]
lst.insert(2, 420)
print(lst)   # [1, 2, 420, 3, 4, 5]

lst.insert(99, 69)
print(lst)   # [1, 2, 420, 3, 4, 5, 69]


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• extend()
• add a list or any other collection datatype(tuple, set, dictionary) to an existing list
• mutates the original list whcih gets extended
'''
num = [1, 2, 3, 4, 5]
s = ['hello', 'world']

num.extend(s)

print(num)  # [1, 2, 3, 4, 5, 'hello', 'world']


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• pop()
• returns the element from the index, default index is last index
• mutates the original list
'''
lst = [1, 2, 3, 4, 5]

print(lst.pop())    # 5
print(lst)          # [1, 2, 3, 4]

print(lst.pop(1))   # 2
print(lst)          # [1, 3, 4]


print('-----------------------------------------------------------------------------------------------------------------------------------')
