'''
• Decorators
• 
'''


def decorator(fx):
  def mfx():
    print('i am decorator')
    fx()
  return mfx


@decorator
def func1():
  print('i am func 1')


func1()
'''
i am decorator
i am func 1
'''

print('-----------------------------------------------------------------------------------------------------------------------------------')


def decorator(fx):
  def mfx(*args):
    print('inside mfx', args)   # inside mfx (2, 4)
    print('inside mfx', *args)  # inside mfx 2 4
    fx(*args)
  return mfx


@decorator
def func1(x, y):
  print(x + y)                  # 6


func1(2, 4)


print('-----------------------------------------------------------------------------------------------------------------------------------')
