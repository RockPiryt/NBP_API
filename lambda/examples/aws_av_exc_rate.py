import json
import requests

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

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



import json
import logging

# AWS Lambda Function Logging in Python - https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    '''Demonstrates Amazon API Gateway Lambda proxy integration. You have full
    access to the request and response payload, including headers and
    status code.
    https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    '''
    logger.debug(event) # Mind logger.setLevel at line 6. Check Event printed at CloudWatch

    #/av_exchange_rate/{user_date}/{curr_code}
    rates = [
        { "id": "1", "user_date": "2024-01-12", "curr_code":"EUR"},
        { "id": "2", "user_date": "2024-03-13", "curr_code":"USD"},
        { "id": "3", "user_date": "2024-02-12", "curr_code":"EUR"}
    ]
    
    
    # Input Format https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    resource = event['resource']
    # Uncomment to print the event
    # print("Received event: " + json.dumps(event, indent=2))

    err = None
    # /pets List all pets
    response_body = {}
    if (resource == "/av_exchange_rate"):
        response_body = {
            "rates": rates
        }
    # /pets/petId find pet by Id    
    elif (resource == "/av_exchange_rate/{user_date}/{curr_code}"):
        USER_DATE = event['pathParameters']['user_date']
        value = next((item for item in pets if item["id"] == str(petId)), False)
        if( value == False ):
            err = "Pet not found"
        else:
            response_body = {
                "pet": value
            }

        
    response =  response_payload(err, response_body)

    return response
  
  
    
'''
In Lambda proxy integration, API Gateway sends the entire request as input to a backend Lambda function. 
API Gateway then transforms the Lambda function output to a frontend HTTP response.
Output Format: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format
'''
def response_payload(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

