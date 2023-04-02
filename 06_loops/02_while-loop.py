
i = 0
while i < 10:
  print(i, end=' ')
  i = i + 1
# 0 1 2 3 4 5 6 7 8 9

print('-----------------------------------------------------------------------------------------------------------------------------------')

'''
• while loop with else
'''

i = 10
while i > 0:
  print(i)
  i = i - 1
else:
  print('Loop done !')
# 10 9 8 7 6 5 4 3 2 1 Loop done !

i = 10
while i > 0:
  print(i)
  i = i - 1
  if i == 5:
    break
else:
  print('Loop done !')
# 10 9 8 7 6

print('-----------------------------------------------------------------------------------------------------------------------------------')


bool = True
while bool:
  inp = input('Enter "0" to stop the loop: ')
  if (inp == '0'):
    bool = False
else:
  print('Successfully exited from the loop')


print('-----------------------------------------------------------------------------------------------------------------------------------')
