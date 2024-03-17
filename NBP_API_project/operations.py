from flask import jsonify
from NBP_API_project import app

@app.route('/api/v1/operation1', methods=['GET'])
def operation1():
    """Given a date (formatted YYYY-MM-DD) and a currency code (list: https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/), provide its average exchange rate"""

    return jsonify({
        'success': True,
        'data': 'Get first info'
    }), 200

@app.route('/api/v1/operation2/<str:curr_code>/<int:last_quo>', methods=['GET'])
def operation2(curr_code, last_quo):
    """Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average)."""

    return jsonify({
        'success': True,
        'data': f'Get second info with {curr_code} and {last_quo}'
    }), 200

@app.route('/api/v1/operation3/<str:curr_code>/<int:last_quo>', methods=['GET'])
def operation3(curr_code, last_quo):
    """Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average)."""

    return jsonify({
        'success': True,
        'data': f'Get third info with {curr_code} and {last_quo}'
    }), 200

