config_file = '../config.yaml'
f_in_test = '../data/test.mat'

import numpy as np
import sys

sys.path.insert(0, '../')
from src import *

a = readMatrix(f_in_test)
b = np.array([[1,2,3],[4,5,6],[7,8,9]])

if np.array_equal(a, b):
    print 'Test array correctly loaded.'
else:
    print 'ERROR: Test array not correctly loaded!'
