import os

path = os.path.join(os.getcwd(), '17_modules', '01_os', 'data')  # D:\Study\Python\17_modules\01_os\data

if (not os.path.exists(path)):
  os.mkdir(path)
else:
  print('Cannot create a file when that file already exists')


print('-----------------------------------------------------------------------------------------------------------------------------------')


for i in range(0, 5):
  try:
    os.mkdir(os.path.join(os.getcwd(), '17_modules', '01_os', 'data', f'data{i}'))
  except FileExistsError as error:
    print(error)


print('-----------------------------------------------------------------------------------------------------------------------------------')


for i in range(0, 5):
  try:
    os.rename(
        os.path.join(os.getcwd(), '17_modules', '01_os', 'data', f'data{i}'),
        os.path.join(os.getcwd(), '17_modules', '01_os', 'data', f'tutorial{i}')
    )
  except FileExistsError as error:
    print(error)


print('-----------------------------------------------------------------------------------------------------------------------------------')
