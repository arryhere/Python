import os

os.chdir(os.path.join(os.getcwd(), '18_file-io'))   # D:\Study\Python\18_file-io

with open('readFile.txt', 'r', encoding="utf-8") as file:
  print(file.read())
  '''
  Hello World !
  I am Python !
  '''
