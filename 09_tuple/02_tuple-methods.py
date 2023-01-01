
'''
• tuple indexing
• tuple(i:j:k]
• i: inclusive j: exclusive, k: jump
• tuple indexing:
  • ('p', 'y', 't', 'h', 'o', 'n')
  •   0    1    2    3    4    5
  •  -6   -5   -4   -3   -2   -1
'''
tuple = ('p', 'y', 't', 'h', 'o', 'n')

print(tuple[0])                  # p
print(tuple[0:])                 # ('p', 'y', 't', 'h', 'o', 'n')
print(tuple[:])                  # ('p', 'y', 't', 'h', 'o', 'n')
print(tuple[:3])                 # ('p', 'y', 't')
print(tuple[:-3])                # ('p', 'y', 't')
print(tuple[0: len(tuple)])      # ('p', 'y', 't', 'h', 'o', 'n')
print(tuple[0:-1])               # ('p', 'y', 't', 'h', 'o')
print(tuple[0: len(tuple) - 1])  # ('p', 'y', 't', 'h', 'o')
print(tuple[2:5])                # ('t', 'h', 'o')
print(tuple[-4:-1])              # ('t', 'h', 'o')
print(tuple[0:len(tuple):3])     # ('p', 'h')
print(tuple[0::3])               # ('p', 'h')


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• count()
• returns the count of the number of items present in the tuple
'''

tuple = (1, 2, 3, 4, 1, 1, 3, 4)
print(tuple.count(1))    # 3
print(tuple.count(4))    # 2
print(tuple.count(44))   # 0


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• index()
• parameters: value, start_index(inclusive), end_index(excusive)
• returns the index of the first occurance of the item in the tuple
• throws error if item not in tuple
'''
tuple = (1, 2, 3, 4, 5, 3, 3, 6, 3)
# print(tuple.index('2'))             # ValueError: tuple.index(x): x not in tuple
print(tuple.index(3))                 # 2
print(tuple.index(3, 4, -1))          # 5


print('-------------------------------------------------------------------------------------------------------------------------')
