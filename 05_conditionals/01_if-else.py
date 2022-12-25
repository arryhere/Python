
age = int(input('Enter your age: '))

if age >= 18:
  print('Congrates you can drink booze')
elif age >= 0 and age < 18:
  print('You cannot drink booze')
else:
  print('Not a valid age')
print('End of Line')


print('-------------------------------------------------------------------------------------------------------------------------')


num = int(input('Enter the value of num: '))

if num < 0:
  print('num is negative')
elif num > 0:
  if (num > 0 and num < 100):
    print('num lies between 0 and 100')
  elif num == 100:
    print('num is 100')
  else:
    print('num is greater than 100')
else:
  print('num is zero')


print('-------------------------------------------------------------------------------------------------------------------------')