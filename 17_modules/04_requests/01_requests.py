import requests

'''
• get request
• 
'''
response = requests.get('https://jsonplaceholder.typicode.com/users')

print(response.json())


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• post request
• 
'''
response = requests.post(
    'https://jsonplaceholder.typicode.com/users',
    json={
        'firstName': 'foo',
        'lastName': 'bar',
    },
    headers={
        'Content-type': 'application/json; charset=UTF-8'
    }
)

print(response.json())


print('-----------------------------------------------------------------------------------------------------------------------------------')
