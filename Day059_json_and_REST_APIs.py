#Day059 - json and REST APIs
city = input('Enter your city: ')

myAPI = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=526f48b568ce72f1ccfdc6cff57d7392"

import requests

response = requests.get(myAPI)

weather_data = response.json()

weather_data['cod']

#http://api.openweathermap.org/data/2.5/weather?q=London&appid=526f48b568ce72f1ccfdc6cff57d7392
#call above API in browser
