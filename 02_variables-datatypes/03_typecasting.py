''' explicit type casting '''
a = '1'
b = '2'

print(a + b)              # 12
print(type(a), type(b))   # <class 'str'> <class 'str'>
print(int(a) + int(b))    # 3


print('-------------------------------------------------------------------------------------------------------------------------')


''' implicit type casting '''
c = 3.7
d = 4
e = c + d

print(type(c), type(d))   # <class 'float'> <class 'int'>
print(e, type(e))         # 7.7 <class 'float'>
