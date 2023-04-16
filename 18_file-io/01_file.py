'''
• File IO

• open() function to open a file, open() returns a file object
• open(filename, mode, encoding=None)
• mode: 
  • r      : open file for reading, gives an error if the file does not exist (default)
  • w      : open file for writing, creates a new file if the file does not exist
  • a      : open for writing, appending to the end of the file if it exists, creates a new file if the file does not exist
  • x      : open for exclusive creation, gives an error if the file already exists

  • +      : open a disk file for updating (reading and writing)
  
  • t      : opens the file in text mode (default)
  • b      : opens the file in binary mode
'''

import os

os.chdir(os.path.join(os.getcwd(), '18_file-io'))   # D:\Study\Python\18_file-io


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• read
'''

try:
  file = open('readFile.txt', 'r')
  print(file)                                       # <_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>
  print(file.read())
  '''
  Hello World !
  I am Python !
  '''
  file.close()
  print(file.closed)                                # True
except FileNotFoundError as error:
  print(error)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• write
'''

file = open('writeFile.txt', 'w')
file.write(f"Hello World !\nI am JavaScript !\n")
file.close()


print('-----------------------------------------------------------------------------------------------------------------------------------')

'''
• append
• 
'''

file = open('appendFile.txt', 'a')
file.write(f"Hello World !\nI am TypeScript !\n")
file.close()


print('-----------------------------------------------------------------------------------------------------------------------------------')
