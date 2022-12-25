
'''
• str[i,j]
• string slicing by index
• i: inclusive j: exclusive

  A   r   i   j   i   t   <space>   D   a   s
  0   1   2   3   4   5      6      7   8   9
-10   9  -8  -7  -6  -5     -4     -3  -2  -1
'''
name = 'Arijit Das'
print(name[9])                # s
print(name[-1])               # s
print(name[0:6])              # Arijit
print(name[:6])               # Arijit
print(name[1:6])              # Arijit
print(name[:])                # Arijit Das
print(name[1:-3])             # rijit<space>
print(name[1:-4])             # rijit
print(name[1:len(name)-4])    # rijit
print(name[-3:-1])            # Da


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• len()
• length of a string
'''
name = 'Arijit Das'
print(len(name))  # 10


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• upper()
• returns a new string with uppercase
'''
name = 'Arijit Das'
print(name.upper())  # ARIJIT DAS


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• lower()
• returns a new string with lowercase
'''
name = 'Arijit Das'
print(name.lower())  # arijit das


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• strip()
• revoves characters from both sides from string (default whitespace)
'''
name = '!!-!!Arijit Das!!-!!'
friend = '    Aditi Jain    '
print(name.strip('!'))  # -!!Arijit Das!!-
print(friend.strip())   # Aditi Jain


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• rstrip, lstrip
• revoves characters from right and left sides respectively from string (default whitespace)
'''
name = '----Arijit----'
print(name.lstrip('-'))  # Arijit----
print(name.rstrip('-'))  # ----Arijit


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• replace()
• replace all occurances if a string with another string
• it is case sensitive
'''
name = 'Arijit ? Arijit'
print(name.replace('Arijit', 'Aditi'))  # Aditi ? Aditi
print(name.replace('arijit', 'Aditi'))  # Arijit ? Arijit


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• split()
• splits the given string at the specified instances and returns the seperated strings as list items
'''
name = 'Linus Torvalds'
print(name.split(' '))  # ['Linus', 'Torvalds']
print(name.split('s'))  # ['Linu', ' Torvald', '']


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• capitalize()
• return a new string with the first character of the string to uppercase and rest characters to lowercase
'''
name = 'arijit Das'
print(name.capitalize())  # Arijit das


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• center()
• returns a new string aligned to the center as per the width given
• width need to be > string length
• fill character can be set, default is whitespace
'''
name = 'Lionel Messi'
print(len(name))              # 12
# ****Lionel Messi**** (20 - 12 = 8, 4 on each side)
print(name.center(20, '*'))


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• count()
• returns the number if times the given value occured in the string
• it is case sensitive
'''
continent = 'Asia'
print(continent.count('a'))  # 1


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• endswith()
• returns boolean based on if the string ends with a given value
'''
name = 'Arijit Das'
print(name.endswith(' Das'))        # True
print(name[7:10])                   # Das
print(name.endswith('Das', 7, 10))  # True


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• find()
• returns index of substring in the string if present, return -1 if not present
'''
name = 'Aditi Jain is a brilliant computer scientist'
print(name.find('is'))  # 11
print(name.find('th'))  # -1


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• index()
• throws an error if substring not present, return index if present
'''
name = 'Aditi Jain is a brilliant computer scientist'
print(name.index('is'))     # 11
# print(name.index('th'))   # ValueError: substring not found


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• isalnum()
• returns true if entire string consists of A-Z,a-z,0-9
• returns false if any other character is present
'''
name = 'ArijitDas99'
friend = 'Arijit Das99'
print(name.isalnum())     # True
print(friend.isalnum())   # False


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• isalpha
• returns true if entire string consists of A-Z,a-z
• eturns false if any other character is present
'''
name = 'ArijitDas'
friend = 'ArijitDas99'
print(name.isalpha())     # True
print(friend.isalpha())   # False


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• 
• 
'''
