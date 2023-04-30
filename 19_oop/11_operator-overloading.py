'''
• Operator Overloading

• It allows developers to redefine the behavior of mathematical and comparison operators for custom data types
• This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes
• Operator overloading allows you to create more readable and intuitive code
• 
'''


class Tensor:
  def __init__(self, x: int, y: int, z: int) -> None:
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self):
    return f"x: {self.x}, y: {self.y}, z: {self.z}"

  def __add__(self, other):
    return Tensor(self.x + other.x, self.y + other.y, self.z + other.z)

  def __sub__(self, other):
    return Tensor(self.x - other.x, self.y - other.y, self.z - other.z)

  def __mul__(self, other):
    return Tensor(self.x * other.x, self.y * other.y, self.z * other.z)

  def __truediv__(self, other):
    return Tensor(self.x / other.x, self.y / other.y, self.z / other.z)


v1 = Tensor(1, 2, 3)
v2 = Tensor(4, 5, 6)

print(v1)             # x: 1, y: 2, z: 3
print(v2)             # x: 4, y: 5, z: 6

v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2
v6 = v1 / v2

print(v3)             # x: 5, y: 7, z: 9
print(v4)             # x: -3, y: -3, z: -3
print(v5)             # x: 4, y: 10, z: 18
print(v6)             # x: 0.25, y: 0.4, z: 0.5


print('-----------------------------------------------------------------------------------------------------------------------------------')
