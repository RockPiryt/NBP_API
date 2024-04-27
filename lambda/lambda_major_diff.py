import json
import requests

def lambda_handler(event, context):
    """Given a currency code and the number of last quotations N (N <= 255), 
    provide the major difference between the buy and ask rate (every day has different rates)."""

    # Parameters
    BUY_SELL_TABLE = "c"
    NBP_ENDPOINT = f"http://api.nbp.pl/api"
    # extract a currency code and the number of last quotations N from the Lambda service's event object
    CURR_CODE = event['curr_code']
    LAST_QUO = event['last_quo']

    # GET request
    MAJOR_ENDPOINT = f"{NBP_ENDPOINT}/exchangerates/rates/{BUY_SELL_TABLE}/{CURR_CODE}/last/{LAST_QUO}/?format=json"
    response3 = requests.get(url=MAJOR_ENDPOINT)

    # Get data
    data = response3.json()

    end = int(LAST_QUO) - 1

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
    #Round value
    max_diff_round = "{:.4f}".format(max_diff)

    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'success': True,
    'body': json.dumps(f'You chose a currency code:{CURR_CODE} and the number of last quotations: {LAST_QUO}. The major difference between the buy and ask rate is {max_diff_round}')
    }
