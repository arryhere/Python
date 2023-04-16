'''
• Access Modifiers

• Unlike other (*real) programming, Python has almost no support for access modifiers at runtime
• But it does now have pretty good support for access modifiers at "compile time" through linters and type checkers
• These used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance

• Types of access modifiers
  • Public      -> can be used anywhere
  • Protected   -> the attribute/method can only be used in the class where it is defined or its subclasses
  • Private     -> the attribute/method can only be used inside the class

• Python Convention for access modifiers
  • protected   -> single underscore (_)
  • private     -> double underscore (__)

• Name mangling
  • It is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses
  • Names of class-private and superclass-private attributes are transformed by the addition of a (_) and a (__) respectively
  • 
'''


class Base():
  public = 'public_key'
  _protected = 'protected_key'
  __private = 'private_key'

  def getPublic(self):
    return f'Base_public: {self.public}'

  def getProtected(self):
    return f'Base_protected: {self._protected}'

  def getPrivate(self):
    return f'Base_private: {self.__private}'


class Child(Base):
  def getPublic(self):
    return f'Child_public: {self.public}'

  def getProtected(self):
    return f'Child_public: {self._protected}'

  def getPrivate(self):
    return f'Child_public: {self.__private}'


base = Base()
print(base.getPublic())       # Base_public: public_key
print(base.getProtected())    # Base_protected: protected_key
print(base.getPrivate())      # Base_private: private_key
print(base.public)            # public_key
print(base._protected)        # protected_key (lint warn: _protected" is protected and used outside of the class in which it is declared)
print(base.__private)         # AttributeError: 'Base' object has no attribute '__private'
print(base._Base__private)    # private_key

child = Child()
print(child.getPublic())      # Child_public: public_key
print(child.getProtected())   # Child_public: protected_key
print(child.getPrivate())     # AttributeError: 'Child' object has no attribute '_Child__private'
print(child.public)           # public_key
print(child._protected)       # protected_key (lint warn: _protected" is protected and used outside of the class in which it is declared)
print(child.__private)        # AttributeError: 'Child' object has no attribute '__private'
print(child._Base__private)   # private_key


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://jellis18.github.io/post/2022-01-15-access-modifiers-python/
• 
'''
