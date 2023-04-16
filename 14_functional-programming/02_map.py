'''
• map()

• arguments: map(function, iterable, *iterable)
• return an iterator that applies function to every item of iterable, yielding the results
• for additional iterables, function must take that many arguments and is applied to the items from all iterables in parallel
• with multiple iterables, the iterator stops when the shortest iterable is exhausted
• 
'''


def square(x):
  return x * x


res = map(square, [1, 2, 3, 4, 5])
print(list(res))  # [1, 4, 9, 16, 25]

res = map(lambda x, y: x * y, [1, 2, 3, 4, 5], [6, 7])
print(list(res))  # [6, 14]

res = map(lambda x, y, z: x * y * z, [1, 2, 3, 4, 5], [6, 7], [8])
print(list(res))  # [48]

res = map(lambda x, y, z: x * y * z, [], [6, 7], [8])
print(list(res))  # []


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://docs.python.org/3/library/functions.html#map
• 
'''