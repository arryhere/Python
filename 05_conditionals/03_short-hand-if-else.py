'''
• Short-hand if-else

• conditionals in one line
'''


x = int(input('Enter x: '))
y = int(input('Enter y: '))

z =     x - y    if       x > y      else    x + y    if      x < y       else      0
#     (do this) <if> (satisfy this) [else] (do this) <if> (satisfy this) [else] (do this)

print(z)
