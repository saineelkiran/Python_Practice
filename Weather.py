import requests

# Replace YOUR_API_KEY with your actual API key
api_key = 'YOUR_API_KEY'

# Specify the location for which you want to retrieve weather data
city = 'Khammam'
state = 'Telangana'
country = 'India'

# Construct the API request URL
url = f'https://openweathermap.org/find?q=khammam'

# Send the API request and store the response
response = requests.get(url)

# Print the raw JSON response
print(response.json())
