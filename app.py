import requests
from requests import exceptions
from requests.models import HTTPBasicAuth
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
## response.content()  # Return the raw bytes of the data payload
## response.text()  # Return a string repr of the data payload
## response.json()  # Convenient when API returns json

# Using Query Params
query = {'lat': '45', 'lon': '180'}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=query)
print(response.json())

# Create and Modify with POST and PUT
response = requests.post('https://httpbin.org/post', data={'key' : 'value'})


# Update an existing resource
requests.put('https://httpbin.org/put', data={'key' : 'value'})

# Access REST Headers
print(response.headers["date"])

# How to Authenticate to a REST API
requests.get('htttps://api.github.com/user', auth=HTTPBasicAuth('username', 'password'))

# More secure way to Authenticate to a REST API is OAuth
my_headers = {'Authorization': 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)

# Using Sessions to Manage Access Tokens
session = requests.Session()
session.headers.update({'Authorization': 'Bearer {access_token}'})
response = session.get('https://httpbin.org/headers')

# Check for HTTP Errors With Python Requests
response = requests.get("http://api.open-notify.org/astros.json")
if (response.status_code == 200):
    print("The request was success!")
    # code here will run only if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    # code here will react to failed requests

# Alternative way to check for HTTPError
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # code will run if request is successful
except requests.exceptions.HTTPError as error:
    print(error)

# Handling TooManyRedirects
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # code here will run if request is successful
except requests.exceptions.TooManyRedirects as error:
    print(error)

# Handle ConnectionError
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    # code here will only run if the request is successful
except requests.ConnectionError as error:
    print(error)

# Handle Timeout
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=0.00001)
    # code will run if request is successful
except requests.Timeout as error:
    print(error)