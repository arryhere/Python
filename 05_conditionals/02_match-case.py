'''
• match-case

• 
'''


x = int(input('Enter any number b/w -> 1 to 5: '))

match x:
  case 1:
    print('The value of x is ', x)
  case 2:
    print('The value of x is ', x)
  case 3:
    print('The value of x is ', x)
  case 4:
    print('The value of x is ', x)
  case 5:
    print('The value of x is ', x)
  case _ if x < 0:
    print('Enter within the range specifed, also x is negative number')
  case _ if x % 2 == 0:
    print('Enter within the range specifed, also x is even number')
  case _:
    print('Enter within the range specifed, also x is odd number')


print('-----------------------------------------------------------------------------------------------------------------------------------')
