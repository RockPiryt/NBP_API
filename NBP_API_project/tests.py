import requests
from datetime import datetime

# #Get response from API
# response = requests.get(url="http://api.nbp.pl/api/cenyzlota/today")

# #Check staus code
# code = response.status_code
# print(code)

# #Get info about errors (404 - Not Found)
# response.raise_for_status()

# data = response.json()
# print(data)

# cena = data[0]["cena"]
# print(cena)
###############################################################
#tabela A

table = "a"
code = "EUR"
date = "2024-01-12"

endpoint = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/"
response = requests.get(url=endpoint)


code = response.status_code
response.raise_for_status()

data = response.json()
print(data)
av_currency_rate = data['rates'][0]['mid']
print(av_currency_rate)
# currency_euro = response.json()[0]["rates"][7]["currency"]
# mid_euro = response.json()[0]["rates"][7]["mid"]
# print(currency_euro)
# print(mid_euro)

# #____________________Given a date (formatted YYYY-MM-DD)
# user_year = 2021
# user_month = 7
# user_day = 22
# user_date = datetime(year=user_year, month=user_month, day=user_day).strftime("%Y-%m-%d")