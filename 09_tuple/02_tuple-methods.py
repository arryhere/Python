
'''
• tuple indexing
• tuple(i:j:k]
• i: inclusive j: exclusive, k: jump
• tuple indexing:
  • ('p', 'y', 't', 'h', 'o', 'n')
  •   0    1    2    3    4    5
  •  -6   -5   -4   -3   -2   -1
'''
tup = ('p', 'y', 't', 'h', 'o', 'n')

print(tup[0])                   # p
print(tup[0:])                  # ('p', 'y', 't', 'h', 'o', 'n')
print(tup[:])                   # ('p', 'y', 't', 'h', 'o', 'n')
print(tup[:3])                  # ('p', 'y', 't')
print(tup[:-3])                 # ('p', 'y', 't')
print(tup[0: len(tup)])         # ('p', 'y', 't', 'h', 'o', 'n')
print(tup[0:-1])                # ('p', 'y', 't', 'h', 'o')
print(tup[0: len(tup) - 1])     # ('p', 'y', 't', 'h', 'o')
print(tup[2:5])                 # ('t', 'h', 'o')
print(tup[-4:-1])               # ('t', 'h', 'o')
print(tup[0:len(tup):3])        # ('p', 'h')
print(tup[0::3])                # ('p', 'h')


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• count()
• returns the count of the number of items present in the tuple
'''

tup = (1, 2, 3, 4, 1, 1, 3, 4)
print(tup.count(1))    # 3
print(tup.count(4))    # 2
print(tup.count(44))   # 0


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• index()
• parameters: value, start_index(inclusive), end_index(excusive)
• returns the index of the first occurance of the item in the tuple
• throws error if item not in tuple
'''
tup = (1, 2, 3, 4, 5, 3, 3, 6, 3)
# print(tup.index('2'))             # ValueError: tuple.index(x): x not in tuple
print(tup.index(3))                 # 2
print(tup.index(3, 4, -1))          # 5


print('-------------------------------------------------------------------------------------------------------------------------')
