import requests, json
import pytest
from utils.aws_configparser import getApiURL
from utils.api_utils import getAPI_Data, putData

baseURI = getApiURL()
userDate = "2024-01-12"
currCode = "EUR"


# test valid response or response is not empty
def test_getAverageRate_response():
    average_url = baseURI + "av_exchange_rate" + "/" + userDate + "/"+ currCode
    data, resp_status, timeTaken =  getAPI_Data(average_url)
    assert len(data)>0, 'empty response'


# test response body for 'success' key
def test_getAverageRate_successKey():
    average_url = baseURI + "av_exchange_rate" + "/" + userDate + "/"+ currCode
    data, resp_status, timeTaken =  getAPI_Data(average_url)
    assert data['success'] == True

@pytest.mark.res_code
# test response body for 'statusCode' key
def test_getAverageRate_statusCode():
    average_url = baseURI + "av_exchange_rate" + "/" + userDate + "/"+ currCode
    data, resp_status, timeTaken =  getAPI_Data(average_url)
    assert data['statusCode'] == 200
    assert resp_status == 200
    print("Time Taken: ", timeTaken)

# test put data(user date and currency code)
# def test_putDateCurrCode():
#     post_url = baseURI + "/api/v1/create_av_exchange_rate"
#     payload = {'date': '2024-01-12', 'curr_code': 'EUR'}
#     data, resp_status, timeTaken  = putData(payload)
#     assert data['date'] == userDate
#     print(data)