import os

print(os.getcwd())  # D:\Study\Python
os.chdir(os.path.join(os.getcwd(), '17_modules', '01_os'))
print(os.getcwd())  # D:\Study\Python\17_modules\01_os

folders = os.listdir('data')

print(folders)

for folder in folders:
  print(folder, os.listdir(os.path.join('data', folder)))


print('-------------------------------------------------------------------------------------------------------------------------')
