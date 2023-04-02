
'''
• default arguments
'''


def average(x=5, y=5):
  avg = (x + y) / 2
  print(f'The average of {x} and {y} is {avg}')


average()         # The average of 5 and 5 is 5.0
average(5, 9.9)   # The average of 5 and 9.9 is 7.45


def name(firstName='John', middleName='Lee', lastName='Doe'):
  print(f'My name is {firstName} {middleName} {lastName}')


name()                              # My name is John Lee Doe
name('Lionel', 'Andrés', 'Messi')   # My name is Lionel Andrés Messi


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• arguments
'''


def divide(x, y):
  print(f'The division of {x}/{y} is {x/y}')


divide(y=5, x=100)  # The division of 100 / 5 is 20.0


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• variable number of arguments
• *args (Non-Keyword Arguments)
• **kwargs (Keyword Arguments)
'''


def average(*args):
  print(args, type(args))  # (1, 2, 3, 4, 5) <class 'tuple'>

  sum = 0
  for i in args:
    sum = sum + i
  avg = sum / len(args)
  print(f'The average of {args} is {avg}')


average(1, 2, 3, 4, 5)  # The average of (1, 2, 3, 4, 5) is 3.0


def name(**kwargs):
  print(kwargs, type(kwargs))  # {'firstName': 'Lionel', 'middleName': 'Andrés', 'lastName': 'Messi'} <class 'dict'>

  print(f'My name is {kwargs["firstName"]} {kwargs["middleName"]} {kwargs["lastName"]}')


name(firstName='Lionel', middleName='Andrés', lastName='Messi')  # My name is Lionel Andrés Messi


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• return
'''


def add(*num):
  sum = 0
  for i in num:
    sum = sum + i
  return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55


print('-----------------------------------------------------------------------------------------------------------------------------------')
