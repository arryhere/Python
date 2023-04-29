'''
• help()

• arguments: help(request)
• Invoke the built-in help system
• If no argument is given, the interactive help system starts on the interpreter console
• If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic,  
  and a help page is printed on the console
• If the argument is any other kind of object, a help page on the object is generated
• 
'''


print(help())
'''
Welcome to Python 3.11's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.11/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help>
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


print(help(list()))
'''
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.

<...continued>
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


dic = {"name": "Arijit", "age": 22}
print(help(dic))
'''
-----------------------------
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].

<...continued>
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://docs.python.org/3/library/functions.html#help
• 
'''