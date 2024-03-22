from flask import jsonify
import requests
from NBP_API_project import app, db
from NBP_API_project.models import AverageRate, AverageRateSchema, rates_schema


@app.route('/api/v1/av_exchange_rate/<user_date>/<curr_code>', methods=['GET'])
def av_exchange_rate(user_date, curr_code):
    """Given a date (formatted YYYY-MM-DD) and a currency code (list: https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/), provide its average exchange rate"""

    # Parameters
    RATE_TABLE = "a"
    NBP_ENDPOINT = f"http://api.nbp.pl/api"
    USER_DATE = f"{user_date}"
    CURR_CODE = f"{curr_code}"

    # GET request
    AV_EXCHANGE_RATE_ENDPOINT = f"{NBP_ENDPOINT}/exchangerates/rates/{RATE_TABLE}/{CURR_CODE}/{USER_DATE}/"
    response = requests.get(url=AV_EXCHANGE_RATE_ENDPOINT)

    # Check codes
    # code = response.status_code
    response.raise_for_status()

    # Get data
    data = response.json()
    av_currency_rate = data['rates'][0]['mid']

    return jsonify({
        'success': True,
        'data': f'You chose a currency code:{curr_code} and a date (formatted YYYY-MM-DD): {user_date}. Average exchange rate is {av_currency_rate}.'
    }), 200


@app.route('/api/v1/min_max_av/<curr_code>/<int:last_quo>', methods=['GET'])
def min_max_av(curr_code, last_quo):
    """Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average)."""

    # Parameters
    RATE_TABLE = "a"
    CURR_CODE = f"{curr_code}"
    N_quotations = f"{last_quo}"

    # GET request
    MIN_MAX_AV_ENDPOINT = f"http://api.nbp.pl/api/exchangerates/rates/{RATE_TABLE}/{CURR_CODE}/last/{N_quotations}/?format=json"
    response2 = requests.get(url=MIN_MAX_AV_ENDPOINT)

    # Check codes
    # code = response2.status_code
    response2.raise_for_status()

    # Get data
    data = response2.json()

    # Create empty list to store mid rates
    mid_rate_list = []

    # Add rates to list
    end = int(N_quotations) - 1

    for i in range(0, end):
        single_mid_rate = data['rates'][i]['mid']
        mid_rate_list.append(single_mid_rate)

    # Find max and min value
    max_value = max(mid_rate_list)
    min_value = min(mid_rate_list)

    return jsonify({
        'success': True,
        'data': f'You chose a currency code:{curr_code} and the number of last quotations: {last_quo}. The max average value is {max_value} and min average value is {min_value}.'
    }), 200


@app.route('/api/v1/major_diff/<curr_code>/<int:last_quo>', methods=['GET'])
def major_diff(curr_code, last_quo):
    """Given a currency code and the number of last quotations N (N <= 255), provide the major difference between the buy and ask rate (every day has different rates)."""

    # Parameters
    BUY_SELL_TABLE = "c"
    CURR_CODE = f"{curr_code}"
    N_quotations = f"{last_quo}"

    # GET request
    # endpoint_major="http://api.nbp.pl/api/exchangerates/rates/c/usd/last/10/?format=json"
    MAJOR_ENDPOINT = f"http://api.nbp.pl/api/exchangerates/rates/{BUY_SELL_TABLE}/{CURR_CODE}/last/{N_quotations}/?format=json"
    response3 = requests.get(url=MAJOR_ENDPOINT)

    # Check codes
    # code = response3.status_code
    response3.raise_for_status()

    # Get data
    data = response3.json()

    end = int(N_quotations) - 1

    # Create buy rates list
    bids_list = []
    for i in range(0, end):
        single_bid_rate = data['rates'][i]['bid']
        bids_list.append(single_bid_rate)

    # Create ask rates list
    asks_list = []
    for i in range(0, end):
        single_ask_rate = data['rates'][i]['ask']
        asks_list.append(single_ask_rate)

    # Make subtraction
    diff_list = []
    for i in range(0, end):
        difference = asks_list[i]-bids_list[i]
        diff_list.append(difference)

    # Find max difference
    max_diff = max(diff_list)

    return jsonify({
        'success': True,
        'data': f'You chose a currency code:{curr_code} and the number of last quotations: {last_quo}. The major difference between the buy and ask rate is {max_diff}'
    }), 200


#_____________________Endpoints (Database)

@app.route('/api/v1/av_exchange_rates', methods=['GET'])
def get_all_av_exchange_rates():
    """Provide all average exchange rates from DB"""

    av_ex_rates_obj_list = AverageRate.query.all()
    av_rates_schema = AverageRateSchema(many=True)

    return jsonify({
        'success': True,
        'data': av_rates_schema.dump(av_ex_rates_obj_list),
        'number_of_records': len(av_ex_rates_obj_list)
    }), 200

@app.route('/api/v1/av_exchange_rates/<int:rate_id>', methods=['GET'])
def get_single_av_exchange_rate(rate_id):
    """Provide a single average exchange rate from DB."""

    av_ex_rate = AverageRate.query.get_or_404(rate_id, description=f"Rate with id {rate_id} not found.")
    

    return jsonify({
        'success': True,
        'data': rates_schema.dump(av_ex_rate)
    }), 200

@app.route('/api/v1/av_exchange_rate/<user_date>/<curr_code>', methods=['POST'])
def create_single_av_exchange_rate(user_date, curr_code):
    """ Create single record in DB (data: an average exchange rate, a date (formatted YYYY-MM-DD) and a currency code."""

    # Parameters
    RATE_TABLE = "a"
    NBP_ENDPOINT = f"http://api.nbp.pl/api"
    USER_DATE = f"{user_date}"
    CURR_CODE = f"{curr_code}"

    # GET request
    AV_EXCHANGE_RATE_ENDPOINT = f"{NBP_ENDPOINT}/exchangerates/rates/{RATE_TABLE}/{CURR_CODE}/{USER_DATE}/"
    response = requests.get(url=AV_EXCHANGE_RATE_ENDPOINT)

    # Check codes
    # code = response.status_code
    response.raise_for_status()

    # Get data
    data = response.json()
    av_currency_rate = data['rates'][0]['mid']

    # Create single record in DB
    single_av_exchange_rate = AverageRate(rate_date=USER_DATE, currency=CURR_CODE, average=av_currency_rate)
    db.session.add(single_av_exchange_rate)
    db.session.commit()

    return jsonify({
        'success': True,
        'info': f'New record in DB has been created.',
        'data': rates_schema.dump(single_av_exchange_rate)
    }), 200