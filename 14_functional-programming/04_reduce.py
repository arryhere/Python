'''
• reduce()
• arguments: reduce(function, iterable)
• apply function of two arguments cumulatively to the items of iterable, from left to right, to reduce the iterable to a single value
• 
'''

from functools import reduce


def sum(x, y):
  return x + y


res = reduce(sum, [1, 2, 3, 4, 5])
print(res)  # 15

res = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(res)  # 120

res = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 100)
print(res)  # 12000

res = reduce(lambda x, y: x * y, [], 100)
print(res)  # 100


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://docs.python.org/3/library/functools.html#functools.reduce
• 
'''