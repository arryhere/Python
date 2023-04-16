'''
• Comparison Operators / Relational operators

• compares the values. It either returns True or False according to the condition
'''
x = 5
y = 10

greaterThan = x > y
lesserThan = x < y
equalTo = x == y
notEqualTo = x != y
greaterThanOrEqualTo = x >= y
lesserThanOrEqualTo = x <= y

print(greaterThan)              # False
print(lesserThan)               # True
print(equalTo)                  # False
print(notEqualTo)               # True
print(greaterThanOrEqualTo)     # False
print(lesserThanOrEqualTo)      # True


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• is
• Tests object identity
• Returns a Boolean stating whether two objects are the same
• check exact location in memory
'''

x = 4
y = 4
print(x == y)  # True
print(x is y)  # True

x = "python"
y = "python"
print(x == y)  # True
print(x is y)  # True

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True
print(x is y)  # False

x = (1, 2, 3)
y = (1, 2, 3)
print(x == y)  # True
print(x is y)  # True

x = None
y = None
print(x == y)  # True
print(x is y)  # True


print('-----------------------------------------------------------------------------------------------------------------------------------')
