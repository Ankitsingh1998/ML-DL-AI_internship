#Day062 - code challenge Air quality
import requests

pin_code = input('Enter the zip id of your location: ')
country_code = input('Enter your country code as per ISO 3166: ')

geo_api = "http://api.openweathermap.org/geo/1.0/zip?zip="+pin_code+","+country_code+"&appid=526f48b568ce72f1ccfdc6cff57d7392"

geo_response = requests.get(geo_api)

geo_data = geo_response.json()

latitude = geo_data['lat']
longitude = geo_data['lon']

print('Geogoraphical data of your location is: '+str(geo_data))

air_quality_api = "http://api.openweathermap.org/data/2.5/air_pollution?lat="+str(latitude)+"&lon="+str(longitude)+"&appid=526f48b568ce72f1ccfdc6cff57d7392"

air_quality_response = requests.get(air_quality_api)

air_quality_data = air_quality_response.json()

print('Air quality information for your city is: '+str(air_quality_data))
