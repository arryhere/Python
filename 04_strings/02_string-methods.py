
'''
• str[i,j]
• string slicing by index
• i: inclusive j: exclusive

  A   r   i   j   i   t   <space>   D   a   s
  0   1   2   3   4   5      6      7   8   9
-10   9  -8  -7  -6  -5     -4     -3  -2  -1
'''
name = 'Arijit Das'
print(name[9])                # s
print(name[-1])               # s
print(name[0:6])              # Arijit
print(name[:6])               # Arijit
print(name[1:6])              # Arijit
print(name[:])                # Arijit Das
print(name[1:-3])             # rijit<space>
print(name[1:-4])             # rijit
print(name[1:len(name)-4])    # rijit
print(name[-3:-1])            # Da


'''
• len()
• length of a string
'''
name = 'Arijit Das'
print(len(name))  # 10
