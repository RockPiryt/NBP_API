import json
import requests

def lambda_handler(event, context):
    """Given a currency code and the number of last quotations N (N <= 255), 
    provide the max and min average value (every day has a different average)."""

    # Parameters
    RATE_TABLE = "a"
    NBP_ENDPOINT = f"http://api.nbp.pl/api"
    # extract a currency code and the number of last quotations N from the Lambda service's event object
    CURR_CODE = event['curr_code']
    LAST_QUO = event['last_quo']

    # GET request
    MIN_MAX_AV_ENDPOINT = f"{NBP_ENDPOINT}/exchangerates/rates/{RATE_TABLE}/{CURR_CODE}/last/{LAST_QUO}/?format=json"
    response2 = requests.get(url=MIN_MAX_AV_ENDPOINT)

    # Get data
    data = response2.json()

    # Create empty list to store mid rates
    mid_rate_list = []

    # Add rates to list
    for i in range(0, int(LAST_QUO) - 1):
        single_mid_rate = data['rates'][i]['mid']
        mid_rate_list.append(single_mid_rate)

    # Find max and min value
    max_value = max(mid_rate_list)
    min_value = min(mid_rate_list)

    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'success': True,
    'body': json.dumps(f'You chose a currency code:{CURR_CODE} and the number of last quotations: {LAST_QUO}. The max average value is {max_value} and min average value is {min_value}.')
    }

