import pytest
import random
from utils.api_utils import postData
from utils.file_utils import getJsonFromFile
from utils.flask_configparser import getFlaskAppBaseURL
from utils.random_date import created_date

baseURI = getFlaskAppBaseURL()
postUrlPath = 'av_exchange_rate' 

# File with sample data
postJsonFile = "postApiValid.json"

# Create random data to tests
randNum = random.uniform(0.2, 1.4)
randomAvRate = round((float("4.35") + randNum),2)
randomUserDate = created_date


# Fixture to post data 
@pytest.fixture
def post_avRate():
    payload = getPayLoadDict_avRate(userDate=randomUserDate, average_rate=randomAvRate)
    postURL = baseURI + postUrlPath
    post_response = postData(postURL, payload)
    assert post_response.status_code == 201
    data = post_response.json()
    yield data # anything after this tatement, will run as part of teardown, or after the test function is executed

# Function to change data in Json File to create different data to test (diffrent dates and average rate)
def getPayLoadDict_avRate(userDate=None, currCode=None, average_rate=None):
    payload = getJsonFromFile(postJsonFile)
    payload["userDate"] = userDate
    payload["average_rate"] = average_rate
    return payload

