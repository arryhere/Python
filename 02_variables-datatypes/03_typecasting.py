'''
• Typecasting/Type conversion in python
• The conversion of one data type into the other data type is known as type casting
• functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python
• Two Types of Typecasting:
  • Explicit type casting/Explicit Conversion
  • Implicit type casting/Implicit Conversion
'''


'''
• Explicit typecasting
• Typecasting done via developer or programmer's intervention or manually as per the requirement
'''
a = '1'
b = '2'

print(a + b)              # 12
print(type(a), type(b))   # <class 'str'> <class 'str'>
print(int(a) + int(b))    # 3


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• Implicit typecasting
• Data types in Python do not have the same level i.e. ordering of data types is not the same in Python
• Some datatype has higher order, some have lower order
• While performing operations, the lower order datatypes will be converted to higher orderdata types by the Python interpreter
• Python converts a smaller data type to a higher data type to prevent data loss
'''
c = 3.7
d = 4
e = c + d

print(type(c), type(d))   # <class 'float'> <class 'int'>
print(e, type(e))         # 7.7 <class 'float'>


print('-----------------------------------------------------------------------------------------------------------------------------------')
