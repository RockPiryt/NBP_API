import requests, json

# get API call and return response data
def getAPI_Data(url):
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    # response = requests.get(url=url, verify=False, headers=header)
    response = requests.get(url=url, headers=header)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert len(data)>0, 'empty response!!'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken