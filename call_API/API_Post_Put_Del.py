import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


USERNAME = os.getenv("username_pixela")
TOKEN = os.getenv("token_pixela")

###############CREATE USER
user_parameters = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)
# print(response.status_code)

###############CREATE GRAPH

graph_parameters = {
    "id": "graph2",
    "name": "PythonGraph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers={
    "X-USER-TOKEN": TOKEN,
}
# PIXELA_ENDPOINT_GRAPH = "https://pixe.la/v1/users/<username>/graphs"
PIXELA_ENDPOINT_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
response = requests.post(url=PIXELA_ENDPOINT_GRAPH, json=graph_parameters, headers=headers)
print(response.text)
print(response.status_code)