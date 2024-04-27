import configparser
from pathlib import Path

cfgFile = 'flaskqa.ini'
cfgDir = 'config'

configFlaskApp = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE =  BASE_DIR.joinpath(cfgDir).joinpath(cfgFile)
configFlaskApp.read(CONFIG_FILE)



def getFlaskAppBaseURL():
    baseURL = 'http://'+ configFlaskApp['flaskapp']['url'] + ':' + configFlaskApp['flaskapp']['port'] + '/api/' + configFlaskApp['flaskapp']['version']  + '/'
    return baseURL

print(getFlaskAppBaseURL())


