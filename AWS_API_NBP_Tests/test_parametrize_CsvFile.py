import pytest

from utils.aws_configparser import getApiURL
from utils.api_utils import getAPI_fullResponse
from utils.file_utils import getDataAsTuple

baseURI = getApiURL()#'https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/'


dataFileWithStatus = "avAWSApiStatus.csv"
tuplesData = getDataAsTuple(dataFileWithStatus)


# testData only tuple value
# input = [userDate, currCode]

# testing api average for different dates and currCode
@pytest.mark.parametrize("input, status", tuplesData)
def test_getAverage_Status(input, status):
    print(input[0])
    print(input[1])
    avURL = baseURI + "av_exchange_rate" + "/" + input[0] + "/"+ input[1]
    print(avURL)
    resp = getAPI_fullResponse(avURL)
    data = resp.json()
    body_resp = data["body"]
    print(body_resp)
    assert body_resp