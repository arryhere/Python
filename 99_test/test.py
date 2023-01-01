print(bin(45))      #   0b101101
print(bin(~45))     #  -0b101110


a = 55
b = a
b = a - 1

print(a, b)
print(id(a), id(b))