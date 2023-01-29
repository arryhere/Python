'''
• Short-hand if-else
• 
'''

x = int(input('Enter x: '))
y = int(input('Enter y: '))

z = x - y if x > y else x + y if x < y else 0

print(z)
