
text1 = 'Hello my name is {0}, and i am from {1}'
text2 = 'Hello my name is {1}, and i am from {0}'
name = 'Arijit'
country = 'India'

print(text1.format(name, country))  # Hello my name is Arijit, and i am from India
print(text2.format(name, country))  # Hello my name is India, and i am from Arijit


print(f'Hello my name is {name}, and i am from {country}')  # Hello my name is Arijit, and i am from India
print(f'Hello my name is {{name}}, and i am from {{country}}')  # Hello my name is {name}, and i am from {country}


print('-------------------------------------------------------------------------------------------------------------------------')

num = 45.6784999

print(f'The value of num is {num}')  # The value of num is 45.6784999
print(f'The value of num is {num:.2f}')  # The value of num is 45.68


print('-------------------------------------------------------------------------------------------------------------------------')
