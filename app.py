import requests
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

# Access Headers
print(response.headers["date"])