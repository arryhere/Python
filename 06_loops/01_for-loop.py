
'''
• iterating over string
'''

str = 'stirng'
for char in str:
  print(char, end=' ')  # s t i r n g


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• iterating over list
'''

list = ['p', 'y', 't', 'h', 'o', 'n']
for e in list:
  print(e, end=' ')  # p y t h o n

languages = ['Python', 'JavaScript', 'C', 'Java', 'C++']
for l in languages:
  for e in l:
    print(e, end=' ')
  print()
# P y t h o n
# J a v a S c r i p t
# C
# J a v a
# C + +


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• range()
'''

for i in range(10):
  print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9

for i in range(5, 10):
  print(i, end=' ')  # 5 6 7 8 9

for i in range(5, 10, 2):
  print(i, end=' ')  # 5 7 9

for i in range(10, 1, -1):
  print(i, end=' ')  # 10 9 8 7 6 5 4 3 2


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• for loop with else
• else will execute on successfull loop completion, not on break !
'''

for e in range(0, 5):
  print(e)
else:
  print('Loop Done !')
# 0 1 2 3 4 Loop Done !

for e in range(0, 5):
  print(e)
  if e == 3:
    break
else:
  print('Loop Done !')
# 0 1 2 3


print('-----------------------------------------------------------------------------------------------------------------------------------')
