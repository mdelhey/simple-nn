config_file = 'config.yaml'
from src import *

# Go to home dir
goToHome(config_file)

# Wget data.mat
getMyData(config_file, verbose=False)

# Read data.mat
X = readMatrix(config_file)

# Display data

