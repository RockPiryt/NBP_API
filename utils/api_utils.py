import requests, json

# get API call and return response data
def getAPI_Data(url):
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    response = requests.get(url=url, headers=header)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert len(data)>0, 'empty response!!'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


# get API call and return full response 
def getAPI_fullResponse(url):
    header = {'Content-Type': 'application/json'}
    response = requests.get(url=url, headers=header)
    print("\nRequest URL: ", url) 
    # print("Request headers: ", response.request.headers)
    # print("Response headers: ", response.headers)
    return response

# put API call 
def putData(url, body):
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    print("RequestBody: ", json.dumps(body))
    response = requests.put(url=url, headers=header, json=body)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

#post API call 
def postData(url, body):
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    print("RequestBody: ", json.dumps(body))
    response = requests.post(url=url, headers=header, json=body)
    return response

# delete API call 
def deleteData(url):
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    response = requests.delete(url=url, headers=header)
    print(response.request.headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken