from flask import jsonify
import requests
from NBP_API_project import app


AV_TABLE = "a"
NBP_ENDPOINT = f"http://api.nbp.pl/api"


@app.route('/api/v1/av_exchange_rate/<user_date>/<curr_code>', methods=['GET'])
def av_exchange_rate(user_date, curr_code):
    """Given a date (formatted YYYY-MM-DD) and a currency code (list: https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/), provide its average exchange rate"""

    AV_EXCHANGE_RATE_ENDPOINT = f"{NBP_ENDPOINT}/exchangerates/rates/{AV_TABLE}/{curr_code}/{user_date}/"
    response = requests.get(url=AV_EXCHANGE_RATE_ENDPOINT)

    code = response.status_code
    print(code)
    response.raise_for_status()

    data = response.json()
    av_currency_rate = data['rates'][0]['mid']
    print(av_currency_rate)

    return jsonify({
        'success': True,
        'data': f'Average exchange rate for {curr_code} on {user_date} is {av_currency_rate}'
    }), 200

@app.route('/api/v1/operation2/<curr_code>/<int:last_quo>', methods=['GET'])
def operation2(curr_code, last_quo):
    """Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average)."""

    
    return jsonify({
        'success': True,
        'data': f'Get second info with {curr_code} and {last_quo}'
    }), 200

@app.route('/api/v1/operation3/<curr_code>/<int:last_quo>', methods=['GET'])
def operation3(curr_code, last_quo):
    """Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average)."""

    return jsonify({
        'success': True,
        'data': f'Get third info with {curr_code} and {last_quo}'
    }), 200

