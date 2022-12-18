'''
• String are immutable in python
'''


'''
• string concatenation
'''
firstName = 'Arijit'
lastName = 'Das'

print(firstName + ' ' + lastName)  # Arijit Das


'''
• multiline string
'''
greet = '''Hello! 
my name is 
Arijit Das'''

print(greet)  # Hello!  my name is  Arijit Das


'''
• index
'''
print(firstName[0])     # A
print(firstName[3])     # j
print(firstName[3])     # j
# print(firstName[6])   # IndexError: string index out of range


'''
• iterating through string
'''
for x in firstName:
  print(x)  # A r i j i t
