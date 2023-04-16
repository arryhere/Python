'''
• String

• strings are immutable in python
'''


'''
• string concatenation
'''
firstName = 'Arijit'
lastName = 'Das'

print(firstName + ' ' + lastName)  # Arijit Das


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• multiline string
'''
greet = '''Hello! 
my name is 
Arijit Das'''

print(greet)
'''
Hello!
my name is
Arijit Das
'''

print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• index
'''
firstName = 'Arijit'

print(firstName[0])     # A
print(firstName[3])     # j
print(firstName[3])     # j
# print(firstName[6])   # IndexError: string index out of range


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• iterating through string
'''
firstName = 'Arijit'

for x in firstName:
  print(x)  # A r i j i t


print('-----------------------------------------------------------------------------------------------------------------------------------')

'''
• if clause in strings
'''
firstName = 'Arijit'

if 'j' in firstName:
  print('yes')    # yes
else:
  print('no')

print('-----------------------------------------------------------------------------------------------------------------------------------')
