'''
• Hybrid Inheritance

• Hybrid inheritance is a combination of multiple inheritance and single inheritance
• Common example is a diamond shaped inheritance
• 
'''


class Root:
  pass


class A(Root):
  pass


class B(Root):
  pass


class C(A, B):
  pass


print('-----------------------------------------------------------------------------------------------------------------------------------')
