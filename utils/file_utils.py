import json, csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_DATA_DIR = BASE_DIR.joinpath('TestData')

# function to read data from JSON file as JSON
def getJsonFromFile(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        return json.load(file)
    
# print(getJsonFromFile('avAWSApiValid.json'))

"""{
    "userDate": "2024-01-12", 
    "currCode":"EUR"
}"""   
    
# function to read data from CSV file as DICT
def getCSVdataAsDict(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csvfile = csv.DictReader(file)
        dictList = list(csvfile)
    return dictList

# print(getCSVdataAsDict('avAWSApiValid.csv'))

"""[{'userDate': '2024-01-12', 'currCode': ' EUR'}, 
{'userDate': '2024-01-10', 'currCode': ' USD'}, 
{'userDate': '2024-01-09', 'currCode': ' GBP'}]"""

# function to read data from CSV file as LIST  
def getCSVdataAsList(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)# after titles
        lines = list(reader)
    return lines

# print(getCSVdataAsList('avAWSApiStatus.csv'))
"""
[['2024-01-12', ' EUR', ' 200'], 
['2024-01', ' EUR', ' 400'], 
['', ' ', ' 422'], 
['2024-01-09', ' ', ' 422'], 
['', ' GBP', ' 422']
"""

# data_func = getCSVdataAsList('avAWSApiStatus.csv')
# print(data_func)


# return list of tuples, within tuples its 'list of inputs' and a scalar value for output-status
def getDataAsTuple(filename):
    dataList = getCSVdataAsList(filename)
    newList = [(lines[:2], lines[2]) for lines in dataList]
    return newList

# print(getDataAsTuple("avAWSApiStatus.csv"))
"""
[(['2024-01-12', ' EUR'], ' 200'), 
(['2024-01', ' EUR'], ' 400'), 
(['', ' '], ' 422'), 
(['2024-01', ' '], ' 422'), 
(['', ' GBP'], ' 422')]
"""