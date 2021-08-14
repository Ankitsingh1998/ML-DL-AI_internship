#Day060 - json and REST APIs
#get APIs - query string / json
currency_api = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=118dd45c354885aacd1f"

import requests

response1 = requests.get(currency_api)

json_data1 = response1.json()


#post APIs - json / json (httpsbin.org --> http methods)
myAPI = "https://httpbin.org/post"

import json

data = {
 'FirstName':'John',
 'skills':['python', 'sql']
 }

headers = {
    "Content-Type":"application/json",
    "Content-Length":len(data),
    "data":json.dumps(data)
    }


response2 = requests.post(myAPI, data, headers)

json_data2 = response2.json()
