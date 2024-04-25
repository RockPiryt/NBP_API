import requests, json
import pytest
from utils.api_utils import getAPI_Data
from utils.api_configparser import *


# baseURI_av = "https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/av_exchange_rate/{user_date}/{curr_code}"

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

# @pytest.mark.res_code
# test response body for 'statusCode' key
def test_getAverageRate_statusCode():
    average_url = baseURI + "av_exchange_rate" + "/" + userDate + "/"+ currCode
    data, resp_status, timeTaken =  getAPI_Data(average_url)
    assert data['statusCode'] == 200
    assert resp_status == 200
    print("Time Taken: ", timeTaken)


