'''
• Docstrings

• Python docstrings are string literals that appear right after the definition of a function, method, class or module
'''


def square(num):
  '''Function that returns the square of a given number'''
  return num**2


print(square(5))        # 25
print(square.__doc__)   # Function that returns the square of a given number
