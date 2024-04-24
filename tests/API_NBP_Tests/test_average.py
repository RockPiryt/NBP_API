# from utils.myutils import getAPI_Data, putData, deleteData
# from utils.myconfigparser import *

# # baseURI = "https://petstore.swagger.io/v2/pet/"
# petID = "191"

# baseURI = getPetAPIURL()

# def test_getPetById():
#     url = baseURI + petID
#     data, resp_status, timeTaken =  getAPI_Data(url)
#     assert data['id'] == int(petID)
#     assert resp_status == 200
#     print("Time Taken: ", timeTaken)
