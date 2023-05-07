'''
• Multilevel Inheritance

• In multilevel inheritance a derived class inherits from another derived class
• This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class
• 
'''


class Root:

  def info(self):
    print('Root')

  def root(self):
    print('root')


class A(Root):

  def info(self):
    Root.info(self)
    print('A')


class B(A):

  def info(self):
    A.info(self)
    print('B')


b = B()

b.info()
'''
Root
A
B
'''

print(B.mro())  # [<class '__main__.B'>, <class '__main__.A'>, <class '__main__.Root'>, <class 'object'>]


b.root()        # root


print('-----------------------------------------------------------------------------------------------------------------------------------')
