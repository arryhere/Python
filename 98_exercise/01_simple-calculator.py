
x = None
y = None
opr = None

check_x = True
check_y = True
check_opr = True

while check_x:
  x = input('Enter the first number: ')
  try:
    x = float(x)
    print('First number entered successfully !\n')
    check_x = False
  except:
    print('Please anter a valid number !')

while check_y:
  y = input('Enter the second number: ')
  try:
    y = float(y)
    print('Second number entered successfully !\n')
    check_y = False
  except:
    print('Please anter a valid number !')

while check_opr:
  opr = input('Enter your choice of operation: +(add) -(sub) *(mul) /(div) %(modulo) //(floor div) **(exp): ')
  opr_list = ['+', '-', '*', '/', '%', '//', '**']
  opr_res_list = [x+y, x-y, x*y, x/y, x % y, x//y, x**y]

  if opr_list.__contains__(opr):
    opr_index = opr_list.index(opr)
    print('The value of', x, opr, y, 'is:', opr_res_list[opr_index])
    check_opr = False
  else:
    print('Please anter a valid operator !')
