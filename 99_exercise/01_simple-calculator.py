
x = 0
y = 0

check_x = True
check_y = True

while check_x:
  x = input('Enter the first number: ')
  try:
    x = float(x)
    check_x = False
    print('First number entered successfully !\n')
  except:
    print('Please anter a valid number !')

while check_y:
  y = input('Enter the second number: ')
  try:
    y = float(y)
    check_y = False
    print('Second number entered successfully !\n')
  except:
    print('Please anter a valid number !')


print('The value of', x, '+', y, 'is:', x + y)
print('The value of', x, '-', y, 'is:', x - y)
print('The value of', x, '*', y, 'is:', x * y)
print('The value of', x, '/', y, 'is:', x / y)
print('The value of', x, '%', y, 'is:', x % y)
print('The value of', x, '//', y, 'is:', x // y)
print('The value of', x, '**', y, 'is:', x ** y)
