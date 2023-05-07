import time


def calcTime(fx):
  def wrapper(*args):
    start = time.time()
    fx(*args)
    end = time.time()

    print(f"function: {fx.__name__}, execution time: {end - start} seconds")

  return wrapper


@calcTime
def f1(x, y):
  time.sleep(5)
  print(x * y)


@calcTime
def f2(x, y, z):
  time.sleep(10)
  print(x + y + z)


f1(3, 5)      # 15 - function: f1, execution time: 5.000685930252075 seconds
f2(2, 4, 6)   # 12 - function: f2, execution time: 10.000505685806274 seconds


print('-----------------------------------------------------------------------------------------------------------------------------------')
