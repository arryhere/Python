'''
• Walrus Operator

• The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression
• The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements
• 
'''

# print(a = False)  # TypeError: 'a' is an invalid keyword argument for print()
print(a := False)   # False


print('-----------------------------------------------------------------------------------------------------------------------------------')


num = [1, 2, 3, 4, 5]

while ((n := len(num)) > 0):
  print(num.pop())  # 5, 4, 3, 2, 1

print(n)  # 0


print('-----------------------------------------------------------------------------------------------------------------------------------')


fruits = list()

while ((fruit := input('Enter fruit name: ')) != 'quit'):
  fruits.append(fruit)

print(fruits)


print('-----------------------------------------------------------------------------------------------------------------------------------')
