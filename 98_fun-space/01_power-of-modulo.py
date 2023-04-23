num = 12345
numStr = str(num)

list = []
for e in numStr:
  list.insert(0, (num % 10))  # get last element from num and add to list
  num = num // 10             # remove last element from num

print(list)                   # [1, 2, 3, 4, 5]
print(sum(list, 0))           # 15
