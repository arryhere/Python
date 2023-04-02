import os

os.chdir(os.path.join(os.getcwd(), '18_file-io'))   # D:\Study\Python\18_file-io


print('-----------------------------------------------------------------------------------------------------------------------------------')


with open('readFile.txt', 'r', encoding="utf-8") as file:
  print(file.read())
  '''
  Hello World !
  I am Python !
  '''


print('-----------------------------------------------------------------------------------------------------------------------------------')


with open('./readFile.txt', 'r', encoding="utf-8") as f:
  for line in f:
    print(line, end='')
    '''
    Hello World !
    I am Python !
    '''
print()

print('-----------------------------------------------------------------------------------------------------------------------------------')


with open('./readFile.txt', 'r', encoding="utf-8") as f:
  print(list(f))  # ['Hello World !\n', 'I am Python !']


print('-----------------------------------------------------------------------------------------------------------------------------------')
