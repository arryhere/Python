'''
• Local variable
  • variable that is defined within a function and is only accessible within that function
  • it is created when the function is called and is destroyed when the function returns
• Global variable
  • variable that is defined outside of a function and is accessible anywhere in your code file
'''


x = 5                               # global variable


def demo():
  x = 4                             # local variable
  print(f"The value of x is: {x}")


demo()                              # The value of x is: 4

print(f"The value of x is: {x}")    # The value of x is: 5


print('-----------------------------------------------------------------------------------------------------------------------------------')

'''
• global keyword
• global keyword is used to declare that a variable is a global variable and should be accesed from global scope.
'''


y = 5                               # global variable


def demo():
  global y
  y = 4                             # local variable
  print(f"The value of y is: {y}")


demo()                              # The value of y is: 4

print(f"The value of y is: {y}")    # The value of y is: 4


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• locals()
• return a dictionary containing the current scope's local variables
'''

print(__name__)                     # __main__
print(__doc__)
'''
• Local variable
  • variable that is defined within a function and is only accessible within that function
  • it is created when the function is called and is destroyed when the function returns
• Global variable
  • variable that is defined outside of a function and is accessible anywhere in your code file
'''
print(__file__)                     # d:\Study\Python\02_variables-datatypes\04_local-vs-global-variables.py
print(__package__)                  # None
print(__loader__)                   # <_frozen_importlib_external.SourceFileLoader object at 0x0000018F47682F50>
print(__spec__)                     # None
print(__annotations__)              # {}
print(__builtins__)                 # <module 'builtins' (built-in)>


print('-----------------------------------------------------------------------------------------------------------------------------------')
