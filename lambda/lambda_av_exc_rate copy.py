import json
import requests

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    """Given a date (formatted YYYY-MM-DD) and a currency code (list: https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/), provide its average exchange rate"""
    
    # Parameters
    RATE_TABLE = "a"
    NBP_ENDPOINT = f"http://api.nbp.pl/api"
    # extract user_date and curr_code from the Lambda service's event object
    USER_DATE = event['user_date']
    CURR_CODE = event['curr_code']

    # GET request
    AV_EXCHANGE_RATE_ENDPOINT = f"{NBP_ENDPOINT}/exchangerates/rates/{RATE_TABLE}/{CURR_CODE}/{USER_DATE}/"
    response = requests.get(url=AV_EXCHANGE_RATE_ENDPOINT)

    # Get data
    data = response.json()
    av_currency_rate = data['rates'][0]['mid']


    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'success': True,
    'body': json.dumps(f'You chose a currency code:{CURR_CODE} and a date (formatted YYYY-MM-DD): {USER_DATE}. Average exchange rate is {av_currency_rate}.')
    }


