import pytest

from utils.aws_configparser import getApiURL
from utils.api_utils import getAPI_fullResponse

baseURI = getApiURL()#'https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/'

testData = [
    ("2024-01-12", "EUR"),
    ("2024-01-10", "USD"),
    ("2024-01-09", "GBP"),
]

# testing api average for different dates and currCode
@pytest.mark.parametrize("userDate, currCode", testData)
def test_getAverage_Status(userDate, currCode):
    avURL = baseURI + "av_exchange_rate" + "/" + userDate + "/"+ currCode
    resp = getAPI_fullResponse(avURL)
    data = resp.json()
    body_resp = data["body"]
    print(body_resp)
    assert body_resp