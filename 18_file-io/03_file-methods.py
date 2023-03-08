'''
• File Object methods

• read()
• readline()
• readlines()
'''

import os

os.chdir(os.path.join(os.getcwd(), '18_file-io'))   # D:\Study\Python\18_file-io


print('-------------------------------------------------------------------------------------------------------------------------')


with open('./readFile.txt', 'r', encoding="utf-8") as f:
  for line in f:
    print(line, end='')
    '''
    Hello World !
    I am Python !
    '''

print('-------------------------------------------------------------------------------------------------------------------------')


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


print('-------------------------------------------------------------------------------------------------------------------------')


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


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• readlines()
• reads all the lines of the file and returns them as a list of strings
'''
with open('./readFile.txt', 'r', encoding="utf-8") as f:
  print(f.readlines())  # ['Hello World !\n', 'I am Python !']


print('-------------------------------------------------------------------------------------------------------------------------')


