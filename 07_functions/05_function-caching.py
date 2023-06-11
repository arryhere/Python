'''
• Function Caching
• 
'''

import time
from functools import lru_cache


@lru_cache
def compute(num: int):
  time.sleep(5)
  return f'cached ! - {num}'


print(compute(5))
print(compute(4))
print(compute(3))
print(compute(2))
print(compute(1))

print(compute(4))
print(compute(3))

print(compute(0))

'''
cached ! - 5  :wait 5 sec
cached ! - 4  :wait 5 sec
cached ! - 3  :wait 5 sec
cached ! - 2  :wait 5 sec
cached ! - 1  :wait 5 sec

cached ! - 4  :fast cached
cached ! - 3  :fast cached

cached ! - 0  :wait 5 sec
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')
