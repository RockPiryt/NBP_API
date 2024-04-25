import configparser
from pathlib import Path

cfgFile = 'nbpqa.ini'
cfgDir = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE =  BASE_DIR.joinpath(cfgDir).joinpath(cfgFile)


config.read(CONFIG_FILE)

# def getAvApiURL():
#     return (config['average']['url'])

# def getMajorApiURL():
#     return (config['major']['url'])

# def getMinMaxApiURL():
#     return (config['minMax']['url'])

def getApiURL():
    return (config['api_url']['url'])

print(getApiURL())




