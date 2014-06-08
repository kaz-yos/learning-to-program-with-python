### 2014-06-08 Python meetup beginner

import stuff

print(stuff.number)
print(stuff.age)
print(stuff.rate)

print(stuff.capitalizeWords("hello I am a hoser."))




### Standard libraries

## math
## Implemented in C and built into Python itself
import math
## constants
math.pi
math.e
## math
math.sqrt(5)
math.pow(6, 3)



## random
import random
## a random number
random.randint(3, 1000)
##
random.seed(10)
random.randint(3, 1000)
random.randint(3, 1000)
random.randint(3, 1000)
## 
random.seed(10)
random.randint(3, 1000)
random.randint(3, 1000)
random.randint(3, 1000)

m = [1,2,3,4,5]
random.shuffle(m)
m


m = ["a","b","c","d","e"]
random.sample(m)
m



## time
import time
time.asctime()
time.strftime("The weekday is %A")
## return an object
the_time = time.localtime()
the_time.tm_year

time.sleep(5)
