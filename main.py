config_file = 'config.yaml'

from src import *

# Go to home dir
goToHome(config_file, verbose=False)

# Wget data.mat
getMyData(config_file)

# 
