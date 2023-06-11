'''
• Multithreading
• 
'''

import time
import threading


def func1(sec):
  time.sleep(sec)
  print('func1')


def func2(sec):
  time.sleep(sec)
  print('func2')


def func3(sec):
  time.sleep(sec)
  print('func3')


'''
start = time.perf_counter()
func1(5)
func2(2)
func3(1)
end = time.perf_counter()
print(end - start)  # 8sec
'''

start = time.perf_counter()
t1 = threading.Thread(target=func1, args=[5])
t2 = threading.Thread(target=func2, args=[2])
t3 = threading.Thread(target=func3, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
end = time.perf_counter()
print(end - start)  # 5sec


print('-----------------------------------------------------------------------------------------------------------------------------------')
