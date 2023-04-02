'''
• File Object methods

• read()
• readline()
• readlines()
• write()
• writelines()
• seek()
• tell()
'''

import os

os.chdir(os.path.join(os.getcwd(), '18_file-io'))   # D:\Study\Python\18_file-io


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• read()
• reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode)
• size is an optional numeric argument
• when size is omitted or negative, the entire contents of the file will be read and returned
• If the end of the file has been reached, f.read() will return an empty string ('')
'''
with open('./readFile.txt', 'r', encoding="utf-8") as f:
  print(f.read())
  '''
  Hello World !
  I am Python !
  '''


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• readline()
• reads a single line from the file
• a newline character (\n) is left at the end of the string and is only omitted on the last line of the file if the file doesn’t end in a newline
• if f.readline() returns an empty string, the end of the file has been reached
'''
with open('./readFile.txt', 'r', encoding="utf-8") as f:
  print(f.readline())  # Hello World !\n
  print(f.readline())  # I am Python
  print(f.readline())  # ''
  print(f.readline())  # ''

with open('./readFile.txt', 'r', encoding="utf-8") as g:
  while True:
    file = g.readline()
    if file == '':
      break
    print(file)
    '''
    Hello World !
    (\n)
    I am Python !
    '''


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• readlines()
• reads all the lines of the file and returns them as a list of strings
'''
with open('./readFile.txt', 'r', encoding="utf-8") as f:
  print(f.readlines())  # ['Hello World !\n', 'I am Python !']


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• write()
• writes the contents of string to the file
• returns the number of characters written
'''
with open('./writeFile.txt', 'w', encoding="utf-8") as f:
  count = f.write(f"Hello World !\nI am JavaScript !\n")
  print(count)  # 32


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• writelines()
• writes a sequence of strings to a file
• sequence can be any iterable object, such as a list or a tuple
'''
with open('./writeFile.txt', 'w', encoding="utf-8") as f:
  f.writelines(['Hello World !\n', 'I am JavaScript !\n'])


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• seek()
• takes 2 args: offset, whence
• whence value of 0: beginning of the file (default), 1: current file position, 2: end of the file as the reference point
• position is computed from adding offset to a reference point
• If the file is opened in text mode (without b), only offsets returned by tell() are legal
  Use of other offsets causes undefined behavior
'''
with open('./readFile.txt', 'r', encoding="utf-8") as f:
  print(f.read(1))      # H
  print(f.read(1))      # e
  f.seek(0)             # Go to the 0th byte in the file
  print(f.read(1))      # H
  f.seek(2)             # Go to the 2nd byte in the file
  print(f.read(1))      # l

with open('./readFile.txt', 'rb') as f:
  f.seek(-3, 2)         # Go to the 3rd byte brfore end in the file
  print(f.read(1))      # b'n'

with open('./readFile.txt', 'rb') as f:
  print(f.read(1))      # b'H'
  print(f.read(1))      # b'e'
  f.seek(4, 1)
  print(f.read(1))      # b'W'


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• tell()
•  returns an integer giving the file object’s current position in the file
• represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode
'''
with open('./readFile.txt', 'r', encoding="utf-8") as f:
  print(f.tell())   # 0
  f.read(1)         # H
  f.read(1)         # e
  f.read(1)         # l
  print(f.tell())   # 3


print('-----------------------------------------------------------------------------------------------------------------------------------')

'''
• truncate()
• truncate the file to specific bytes
'''
with open('./writeFile.txt', 'r+', encoding="utf-8") as f:
  f.read()
  count = f.truncate(2)
  print(count)  # 2


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• References
• https://stackoverflow.com/questions/21533391/seeking-from-end-of-file-throwing-unsupported-exception
• 
'''
