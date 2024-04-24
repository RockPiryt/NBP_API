import requests, json

baseURI = "https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/av_exchange_rate"
# baseURI = "https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/av_exchange_rate/{user_date}/{curr_code}"

userDate = "2024-01-12"
currCode = "EUR"

# test valid response or response is not empty
def test_getAverageRate_response():
    url = baseURI + "/" + userDate + "/"+ currCode
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    # response = requests.get(url=url, verify=False, headers=header)
    response = requests.get(url=url, headers=header)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert len(data)>0, 'empty response'


# test response body for 'success' key
def test_getAverageRate_successKey():
    url = baseURI + "/" + userDate + "/"+ currCode
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    response = requests.get(url=url, headers=header)
    data = response.json()
    assert data['success'] == True

# test response body for 'statusCode' key
def test_getAverageRate_statusCode():
    url = baseURI + "/" + userDate + "/"+ currCode
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    response = requests.get(url=url, headers=header)
    data = response.json()
    assert data['statusCode'] == 200


