'''
• Generators

• Generators are a simple and powerful tool for creating iterators
• They are written like regular functions but use the yield statement whenever they want to return data
• Generator function return Generator object which can be used to genrate values one-by-one as we iterate over it
• Generators allows us to create data on-the-fly instead of having to create and store the entire data
• 
'''


def gen():
  for i in range(5):
    yield i


res = gen()

print(next(gen()))  # 0
print(next(gen()))  # 0
print(next(gen()))  # 0
print(next(gen()))  # 0
print(next(gen()))  # 0

print(next(res))    # 0
print(next(res))    # 1
print(next(res))    # 2
print(next(res))    # 3
print(next(res))    # 4
