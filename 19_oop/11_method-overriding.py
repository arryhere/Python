'''
• Polymorphism

• Polymorphism is one of the core concepts of object-oriented programming (OOP)
• It describes situations in which something occurs in several different forms
• In computer science, it describes the concept that you can access objects of different types through the same interface
• Each type can provide its own independent implementation of this interface

• Different types of polymorphism
  • compile-time polymorphism   -> Method overloading
  • runtime polymorphism        -> Method overriding

• Method overloading
  • Python does not support method overloading
  • 

• Method overriding
  • 
'''


class A:

  def info(self):
    print('class A')


class B(A):
  def info(self):
    print('class B')


obj = B()
obj.info()    # class B
