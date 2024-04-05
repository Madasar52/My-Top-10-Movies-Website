import requests

response = requests.get('https://api.themoviedb.org/3/configuration', params={"api_key": '4191337b697b8d8e5c7e86b1bc86e107', "query": 'drive'})
data = response.json()
print(data)