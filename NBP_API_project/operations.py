from flask import jsonify
import requests
from NBP_API_project import app



@app.route('/api/v1/av_exchange_rate/<user_date>/<curr_code>', methods=['GET'])
def av_exchange_rate(user_date, curr_code):
    """Given a date (formatted YYYY-MM-DD) and a currency code (list: https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/), provide its average exchange rate"""

    # URL params
    AV_TABLE = "a"
    NBP_ENDPOINT = f"http://api.nbp.pl/api"
    USER_DATE = f"{user_date}"
    CURR_CODE =f"{curr_code}"

    # GET request
    AV_EXCHANGE_RATE_ENDPOINT = f"{NBP_ENDPOINT}/exchangerates/rates/{AV_TABLE}/{CURR_CODE}/{USER_DATE}/"
    response = requests.get(url=AV_EXCHANGE_RATE_ENDPOINT)

    # Check codes
    # code = response.status_code
    response.raise_for_status()

    # Get data
    data = response.json()
    av_currency_rate = data['rates'][0]['mid']
    
    return jsonify({
        'success': True,
        'data': f'Average exchange rate for {curr_code} on {user_date} is {av_currency_rate}'
    }), 200

@app.route('/api/v1/last_quotations/<curr_code>/<int:last_quo>', methods=['GET'])
def last_quotations(curr_code, last_quo):
    """Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average)."""

    # URL params
    RATE_TABLE = "a"
    CURR_CODE = f"{curr_code}"
    N_quotations = f"{last_quo}"

    # __________________GET request
    LAST_QUO_ENDPOINT = f"http://api.nbp.pl/api/exchangerates/rates/{RATE_TABLE}/{CURR_CODE}/last/{N_quotations}/?format=json"
    response2 = requests.get(url=LAST_QUO_ENDPOINT)

    # __________________Check codes
    # code = response2.status_code
    response2.raise_for_status()


    # __________________Get data
    data = response2.json()

    # Create empty list to store mid rates
    mid_rate_list = []

    # Add rates to list
    end = int(N_quotations) - 1

    for i in range(0,end):
        single_mid_rate = data['rates'][i]['mid']
        mid_rate_list.append(single_mid_rate)
    
    max_value = max(mid_rate_list)
    min_value = min(mid_rate_list)
    
    return jsonify({
        'success': True,
        'data': f'The max is {max_value} and min is {min_value} average value for {curr_code} and {last_quo}'
    }), 200

@app.route('/api/v1/major_diff/<curr_code>/<int:last_quo>', methods=['GET'])
def major_diff(curr_code, last_quo):
    """Given a currency code and the number of last quotations N (N <= 255), provide the major difference between the buy and ask rate (every day has different rates)."""

    # URL params
    BUY_SELL_TABLE = "c"
    CURR_CODE = f"{curr_code}"
    N_quotations = f"{last_quo}"

    # GET request
    # endpoint_major="http://api.nbp.pl/api/exchangerates/rates/c/usd/last/10/?format=json"
    MAJOR_ENDPOINT = f"http://api.nbp.pl/api/exchangerates/rates/{BUY_SELL_TABLE}/{CURR_CODE}/last/{N_quotations}/?format=json"
    response3 = requests.get(url=MAJOR_ENDPOINT)

    # code = response3.status_code
    response3.raise_for_status()

    data = response3.json()
    # print(data)

    end = int(N_quotations) - 1

    # buy = bids
    # sell = ask

    # Create buy rates list
    bids_list = []
    for i in range(0,end):
        single_bid_rate = data['rates'][i]['bid']
        bids_list.append(single_bid_rate)

    # Create ask rates list
    asks_list = []
    for i in range(0,end):
        single_ask_rate = data['rates'][i]['ask']
        asks_list.append(single_ask_rate)


    return jsonify({
        'success': True,
        'data': f'Get third info with {curr_code} and {last_quo}'
    }), 200

