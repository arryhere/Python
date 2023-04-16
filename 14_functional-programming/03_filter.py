'''
• filter()

• arguments: filter(function, iterable)
• returns an iterator from those elements of iterable for which function is true
• if function is None, the identity function is assumed i.e, all elements of iterable that are false are removed
'''


def isEven(x):
  return x % 2 == 0


res = filter(isEven, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(res))  # [2, 4, 6, 8, 10]

res = filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(res))  # [1, 3, 5, 7, 9]

res = filter(lambda x: x % 2 != 0, [])
print(list(res))  # []


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://docs.python.org/3/library/functions.html#filter
• 
'''
