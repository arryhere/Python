'''
• DataTypes

• datatype specifies the type of value a variable holds
• python has the following datatypes:
  • int, float, complex
  • string
  • boolean
  • Sequenced data: list, tuple, set
  • Mapped data: dict (dictionary)
  • None
'''

a = 12345
b = 12.345
c = complex(3, 4)
d = 'Arijit'
e = True
f = [1, '2', True]
g = (1, '2', True)
h = {'key': 'value', 'age': 22}
i = None


print(a, type(a), sep=': ')    # 12345: <class 'int'>
print(b, type(b), sep=': ')    # 12.345: <class 'float'>
print(c, type(c), sep=': ')    # (3+4j): <class 'complex'>
print(d, type(d), sep=': ')    # Arijit: <class 'str'>
print(e, type(e), sep=': ')    # True: <class 'bool'>
print(f, type(f), sep=': ')    # [1, '2', True]: <class 'list'>
print(g, type(g), sep=': ')    # (1, '2', True): <class 'tuple'>
print(h, type(h), sep=': ')    # {'key': 'value', 'age': 22}: <class 'dict'>
print(i, type(i), sep=': ')    # None: <class 'NoneType'>


print('-----------------------------------------------------------------------------------------------------------------------------------')
