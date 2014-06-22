## 2014-06-22 advanced modules

import sys
import os
import math
math.pi

sys.path

import modulea

print("main file being run")
print(modulea.x)
print(modulea.__doc__)
print(modulea.calculateOdds.__doc__)


##
print("__name__ is ", __name__)

## True if run by its own
## module name is returned if imported
if __name__ == "__main__":
    print("This got run on its own")
else:
    print("This got imported")


##
print(modulea.content)
print(modulea.x)
print(modulea.printNumber())

## one thing from the module, not from 
from modulea import printNumber
printNumber()

## This can be dangerous
## from math import *


## Giving an abbreviation
# import pandas as pd


## os module
## interacting with the operating system
## os.getcwd() pwd
## os.listdir() ls
## os.chdir() cd
## os.mkdir() mkdir
## 
## sys module
## get the information about the system
sys.version
sys.platform

## 
sys.args
