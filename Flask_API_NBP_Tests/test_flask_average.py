import requests, json
import pytest
from utils.flask_configparser import getFlaskAppBaseURL
from utils.api_utils import getAPI_Data, putData

userDate = "2024-01-10"
currCode = "EUR"
baseURI = getFlaskAppBaseURL()#'http://127.0.0.1:5000/api/v1/'
getURL = baseURI + "av_exchange_rate"+ "/" + userDate + "/"+ currCode
postURL = baseURI + "create_av_exchange_rate"

# test valid response or response is not empty
def test_getAverageRate_response():
    data, resp_status, timeTaken =  getAPI_Data(getURL)
    assert len(data)>0, 'empty response'


# test response body for 'success' key
def test_getAverageRate_successKey():
    data, resp_status, timeTaken =  getAPI_Data(getURL)
    assert data['success'] == True

@pytest.mark.res_code
# test response body for 'statusCode' key
def test_getAverageRate_statusCode():
    data, resp_status, timeTaken =  getAPI_Data(getURL)
    assert resp_status == 200
    print("Time Taken: ", timeTaken)

# # test put data(user date and currency code)
# def test_putDateCurrCode():
#     payload = {'date': '2024-01-12', 'curr_code': 'EUR'}
#     data, resp_status, timeTaken  = putData(postURL, payload)
#     assert data['date'] == userDate
#     print(data)