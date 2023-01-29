'''
• Raising custom errors
• 'raise' keyword to raise custom errors
'''

try:
  num = int(input('Enter the value of num: '))
  try:
    if num < 0 or num > 10:
      raise ValueError('invalid input range')
    else:
      print(f'num: {num}')
  except ValueError as e:
    print('inner exception: ', e)   # inner exception: <error>
except Exception as e:
  print('outer exception: ', e)     # outer exception: <error>


print('-------------------------------------------------------------------------------------------------------------------------')



