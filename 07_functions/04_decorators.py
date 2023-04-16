'''
• Decorators
• It is a function that takes a function as argument and extends the behavior of the latter function without explicitly modifying it
• It allows a user to add new functionality to an existing object without modifying its structure
• It provide a simple syntax for calling Higher-order functions
• Higher-order functions
  • takes one or more functions as arguments
  • returns a function as its result
'''


import time


def decorator(fx):
  def wrapper():
    print('i am decorator')
    fx()
  return wrapper


@decorator
def func():
  print('i am func')


func()
'''
i am decorator
i am func
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


def numeratorAlwaysGTdenomenator(fx):
  def wrapper(x, y):
    if (x < y):
      x, y = y, x
    return fx(x, y)
  return wrapper


@numeratorAlwaysGTdenomenator
def division(x, y):
  return x / y


print(division(2, 4))  # 2.0


print('-----------------------------------------------------------------------------------------------------------------------------------')


def doubleArgs(fx):
  def wrapper(*args):
    print('inside wrapper', args, *args)
    return fx(*args, *args)
  return wrapper


@doubleArgs
def add(*args):
  res = 0
  for e in args:
    res += e
  return res


print(add(2, 4, 8))

'''
inside wrapper (2, 4)
inside wrapper 2 4
6
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


def calcTime(fx: function):
  def wrapper():
    start = time.time()
    fx()
    end = time.time()
    duration = end - start
    print(f'function: {fx.__name__}, execution time: {duration}')
  return wrapper

@calcTime
def slowFunc():
  time.sleep(10)

@calcTime
def fastFunc():
  time.sleep(2)

slowFunc()
fastFunc()


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://www.youtube.com/watch?v=BE-L7xu8pO4
• 
'''