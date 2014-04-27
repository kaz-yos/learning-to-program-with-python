### 2014-04-27 Learning to program in Python: Beginner session

### 
### Assignment: Giving a name
myVariable = 50 # statement to assign a value, no return value
myVariable      # now it is an expression

yourHourse = 25
yourHourse

## this is an error because of the indentation
# (space here) x = 4
#

m = 20 * 4 + 3
m


### 
### strings are text always quoted

"this is a string"      # value is itself

## operator overload for string concatenation
"I am" + "Iron Man!"

a = "      "
a

## * works, too
"I am k! " * 3

## type error
"kazuki" - "k"

###
### type
## Check data type
myVar = "Johnny"
type(myVar)
type(1)

## order of evaluation
type(4 + 4)

## no auto-conversion
"piano" + 5

## need to convert explicit
"piano" + str(5)

type(str(20))

## evaluation starts inside  first
str(3 * 4 + 1)
