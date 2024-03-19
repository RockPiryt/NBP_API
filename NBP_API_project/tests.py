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

# ___________________________Average exchange rate

# # URL params
# table = "a"
# code = "EUR"
# date = "2024-01-12"

# # GET request
# endpoint = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/"
# response1 = requests.get(url=endpoint)

# # code = response.status_code
# # print(code)
# response1.raise_for_status()

# data = response1.json()
# av_currency_rate = data['rates'][0]['mid']
# # print(av_currency_rate)


# ___________________________Min and max value

# # URL params
# RATE_TABLE = "a"
# CURR_CODE = "GBP"
# N_quotations = "15"

# # GET request
# # endpoint_last="http://api.nbp.pl/api/exchangerates/rates/a/gbp/last/10/?format=json"
# LAST_QUO_ENDPOINT = f"http://api.nbp.pl/api/exchangerates/rates/{RATE_TABLE}/{CURR_CODE}/last/{N_quotations}/?format=json"
# response2 = requests.get(url=LAST_QUO_ENDPOINT)

# # code = response2.status_code
# # print(code)
# response2.raise_for_status()

# data = response2.json()
# # print(data)

# end = int(N_quotations) - 1

# mid_rate_list = []
# for i in range(0,end):
#     single_mid_rate = data['rates'][i]['mid']
#     mid_rate_list.append(single_mid_rate)
#     # print(single_mid_rate)


# max_value = max(mid_rate_list)
# print(max_value)
# min_value = min(mid_rate_list)
# print(min_value)

# ___________________________Major difference between the buy and ask rate

# URL params
BUY_SELL_TABLE = "c"
CURR_CODE = "USD"
N_quotations = "10"

# GET request
# endpoint_major="http://api.nbp.pl/api/exchangerates/rates/c/usd/last/10/?format=json"
MAJOR_ENDPOINT = f"http://api.nbp.pl/api/exchangerates/rates/{BUY_SELL_TABLE}/{CURR_CODE}/last/{N_quotations}/?format=json"
response3 = requests.get(url=MAJOR_ENDPOINT)

# code = response3.status_code
# print(code)
response3.raise_for_status()

data = response3.json()
# print(data)

end = int(N_quotations) - 1

# buy = bids
# sell = ask

bids_list = []
for i in range(0,end):
    single_bid_rate = data['rates'][i]['bid']
    bids_list.append(single_bid_rate)
    # print(single_bid_rate)

print(bids_list)

asks_list = []
for i in range(0,end):
    single_ask_rate = data['rates'][i]['ask']
    asks_list.append(single_ask_rate)
    # print(single_ask_rate)

print(asks_list)







# #____________________Given a date (formatted YYYY-MM-DD)
# user_year = 2021
# user_month = 7
# user_day = 22
# user_date = datetime(year=user_year, month=user_month, day=user_day).strftime("%Y-%m-%d")