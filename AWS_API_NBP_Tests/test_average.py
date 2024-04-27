import requests, json
import pytest
from utils.aws_configparser import getApiURL
from utils.api_utils import getAPI_fullResponse

userDate = "2024-01-12"
currCode = "EUR"

baseURI = getApiURL()#'https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/'
avURL = baseURI + "av_exchange_rate" + "/" + userDate + "/"+ currCode


# test valid response or response is not empty
def test_getAverageRate_response():
    response =  getAPI_fullResponse(avURL)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert len(data)>0, 'empty response'


# test response body for 'success' key
def test_getAverageRate_successKey():
    data =  getAPI_fullResponse(avURL)
    assert data['success'] == True

@pytest.mark.res_code
# test response body for 'statusCode' key
def test_getAverageRate_statusCode():
    response = getAPI_fullResponse(avURL)
    assert response.status_code == 200
    

# test response body for time taken
def test_getAverageRate_statusCode():
    response = getAPI_fullResponse(avURL)
    timeTaken = response.elapsed.total_seconds()
    print("Time Taken: ", timeTaken)
    assert timeTaken < 1
    

