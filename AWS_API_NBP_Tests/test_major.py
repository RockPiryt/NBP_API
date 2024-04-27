import json
import pytest
from utils.aws_configparser import getApiURL
from utils.api_utils import getAPI_fullResponse

last_quo = "10"
currCode = "EUR"

baseURI = getApiURL()#'https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/'
majorURL = baseURI + "major_diff" + "/" + currCode + "/"+ last_quo

# test valid response or response is not empty
def test_getMajor_response():
    response =  getAPI_fullResponse(majorURL)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert len(data)>0, 'empty response'


# test response body for 'success' key
def test_getMajor_successKey():
    response =  getAPI_fullResponse(majorURL)
    data = response.json()
    assert data['success'] == True

@pytest.mark.res_code
# test response body for 'statusCode' key
def test_getMajor_statusCode():
    response = getAPI_fullResponse(majorURL)
    assert response.status_code == 200
    

# test response body for time taken
def test_getMajor_timeTaken():
    response = getAPI_fullResponse(majorURL)
    timeTaken = response.elapsed.total_seconds()
    print("Time Taken: ", timeTaken)
    assert timeTaken < 1