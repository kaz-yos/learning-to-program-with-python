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



###
### Comparisons

4 < 5
str(4 < 5)

## spacing encouraged
2 == 2


## strings
"H" == "h"
"g " == "g"


###
### print()
print("hello!")

## no quote
print(5)


###
### input() function for taking information from the user
## this asks for 
## a = input("What's your name? ")


###
### Conditionals
if 3 < 7:
    print("hi!")

## Reverse conversin
int("5")



###
### example program: ATM
## Create variables
user_pin = 5544
user_balance = 500

## define an ATM
pin_attempt = input("enter your PIN ")
pin_attempt = int(pin_attempt)  # convert to int

if pin_attempt == user_pin:
    amount_to_withdraw = int(input("How much would youlike to withdraw? "))
    if amount_to_withdraw <= user_balance:
        print("Disbursing " + str(amount_to_withdraw))
        print("Remaining balance: " + str(user_balance - amount_to_withdraw))
    else:
        print("Insufficient funds.")
else:
    print("Invalid PIN.")

print("Transaction concluded.")
