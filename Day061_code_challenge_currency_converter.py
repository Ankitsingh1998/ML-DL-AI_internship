#Day061 - code challenge currency converter
import requests

currency_api = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=118dd45c354885aacd1f"

response = requests.get(currency_api)

json_data = response.json()

from datetime import date

today_date = date.today()

print("1 USD is equivalent to: "+'Rs'+str(round(json_data['USD_INR'], 4))+' as of '+str(today_date.day)+'/'+str(today_date.month)+'/'+str(today_date.year)+'.')

