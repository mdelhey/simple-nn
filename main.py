config_file = 'config.yaml'

# Go to home dir
from goToHome import goToHome
goToHome()

# Get data
from getMyData import getMyData
getMyData(config_file)
