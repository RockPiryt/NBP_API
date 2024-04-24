import requests, json
from utils.api_utils import getAPI_Data

baseURI = "https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/av_exchange_rate"
# baseURI = "https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/av_exchange_rate/{user_date}/{curr_code}"

userDate = "2024-01-12"
currCode = "EUR"

# test valid response or response is not empty
def test_getAverageRate_response():
    url = baseURI + "/" + userDate + "/"+ currCode
    data, resp_status, timeTaken =  getAPI_Data(url)
    assert len(data)>0, 'empty response'


# test response body for 'success' key
def test_getAverageRate_successKey():
    url = baseURI + "/" + userDate + "/"+ currCode
    data, resp_status, timeTaken =  getAPI_Data(url)
    assert data['success'] == True

# test response body for 'statusCode' key
def test_getAverageRate_statusCode():
    url = baseURI + "/" + userDate + "/"+ currCode
    data, resp_status, timeTaken =  getAPI_Data(url)
    assert data['statusCode'] == 200
    assert resp_status == 200
    print("Time Taken: ", timeTaken)


