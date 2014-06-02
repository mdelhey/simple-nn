f_in_make = '../data/makeTestData.m'
f_in_test = '../data/test.mat'

import numpy as np
import sys, subprocess

sys.path.insert(0, '../')
from src import *

# Generate test data
cmd_cd = 'cd ../data/'
cmd_octave = 'octave ' + f_in_make
cmd = cmd_cd + ';' + cmd_octave
subprocess.call(cmd, shell=True)

# Read matricies
a = readMatrix(f_in_test)
b = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Check if equal
if np.array_equal(a, b):
    print 'Test array correctly loaded.'
else:
    print 'ERROR: Test array not correctly loaded!'
