'''
• Error/Exception Handling
• Exception handling is the process of responding to unwanted or unexpected events when a computer program runs
• Exception handling deals with these events to avoid the program or system from crashing
• Exceptions disrupt the normal flow of the program
'''

'''
print('start')                                # start
num = float(input('Enter a valid number: '))  # ValueError: could not convert string to float: 'ewewe'
print(f'num: {num}')                          # program execution stps
print('end')
'''

print('-------------------------------------------------------------------------------------------------------------------------')

'''
• handling exceptions
'''

print('start')                                # start

try:
  num = float(input('Enter a valid number: '))
  print(f'num: {num}')
except Exception as error:
  print(type(error), error)                   # <class 'ValueError'> could not convert string to float: <num>

print('end')                                  # end


print('-------------------------------------------------------------------------------------------------------------------------')

'''
• handling multiple exceptions
'''

print('start')                                # start

try:
  num = int(input('Enter a valid number: '))
  arr = [1, 2, 3, 4, 5]
  print(f'arr[{num}]: {arr[num]}')
except ValueError as valueError:
  print('valueError', valueError)             # valueError invalid literal for int() with base 10: <num>
except IndexError as indexError:
  print('indexError', indexError)             # indexError list index out of range

print('end')                                  # end


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• finally, Clean-up Actions
• finally clause runs whether or not the try statement produces an exception
'''


def test():
  try:
    num = int(input('Enter a valid number: '))
    return f'num: {num}'
  except Exception as error:
    return error
  finally:
    print('cleanup')  # cleanup


print(test())         # <output>


print('-------------------------------------------------------------------------------------------------------------------------')
