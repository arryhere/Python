'''
• enumerate()
• arguments: enumerate(iterable, start=0)
• takes iterable and start-index as arguments, default start-index = 0
• returns tuple of index and element (i, e)
'''


l = [1, 2, 3, 4, 5]

for x in enumerate(l):
  print(x)
'''
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 5)
'''

for i, e in enumerate(l, 0):
  print(i, e)
'''
0 1
1 2
2 3
3 4
4 5
'''


print('-------------------------------------------------------------------------------------------------------------------------')


s = 'python'

for i, e in enumerate(s):
  if i == 2:
    print(e)  # t


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://docs.python.org/3/library/functions.html#enumerate
• 
'''
