##  This is our main program.

# Start with import statements
import stuff

print(stuff.pi)
print(stuff.add(4,15))


## Standard libraries

## Pseudorandom number time since 1970-01-01
import random

random.randint(3,486)
myList = ["heky","cheeta","cougar","plant"]
random.choice(myList)
myList
random.shuffle(myList)
myList


## math module
import math
math.pi
math.e
math.sqrt(40)
round(math.sqrt(40), 3 )


import webbrowser
webbrowser.open("http://www.google.com")

## only pi is imported 
from math import pi
pi

## Only add is imported. Nothing else including the math module itself not imported
from stuff import add
add(5, 7)

pi = 5
from math import pi
pi

