### 2014-04-27 Learning to program in Python: Advanced class

### 
### interactive shell
print("Hello World!")

### 
### types
type(1)
type(1.0)
type(True)
type("hello")


###
### Math

## division
3 / 2
3 // 2

## increment
n = 3
n +=  1
n


user_input = input("this is the prompt!")
user_input


## Boolian conversion
bool(0)
bool(1)

## this is False
5 == "5"
## this is not 
5 > "5"



print("kazuki \
" +
"kazuki")

### 
### ATM example again

user_PIN = 5544
user_balance = 500

PIN_attempt = int(input("What is your PIN? "))

if PIN_attempt == user_PIN:
    ## Do something
    amount_to_withdraw = int(input("How much would you like to withdraw?"))
    if amount_to_withdraw <= user_balance:
        user_balance = user_balance - amount_to_withdraw
        print("Disbursing $" + str(amount_to_withdraw))
        print("Remaining balance: $" + str(user_balance))
    else:
        print("Insufficient funds.")
else:
    print("Invalid PIN")
    
print("Transaction concluded.")


"""kazuki
comment
commment"""


n = 0
while n < 10:
    print(n)
    n += 1    


###
### List and OOP
myList = []
myList
type(myList)

myList.append(5)
myList
myList.append(30)
myList

myList.clear()
myList

myList = [1, 2, 7, 2, 3,
          76, 23, 2 ,0 ,-3
          -5]
myList[0]
myList[5]
myList[15]      # no such element

myList.sort()
myList


###
### for loop

for elt in myList:
    print(elt)

## range
range(30)
list(range(30))

for elt in list(range(30)):
    print(elt)

for elt in range(5,15):
    print(elt)

## contains?
23 in myList
"c" in "line"
"ca" in "carcinoma"

## 
"piranha".index("pir")
## first match only
"piranha".index("a")

m = "piranha"
m[-1]
m[-2]
m[1:2]

## strings are immutable, no partial assignment.
m[1:2] = 3

## Function
x = [3, 4, "moose"]
sum(x)

## length
len(x)

## Function
x = [4, 3, -2, 7]
sorted(x)
x
x.sort()
x
x.reverse()
x
reversed(x)
list(reversed(x))
x.sort()

### 
### functions

def name_of_func(args,arg1):
    ## body of function
    pass        # do nothing

## add function
def add(a,b):
    return a + b

add(4,-3)

def capitalize(some_string):
    result = some_string[0].upper()     # method
    result += some_string[1:]
    return result

capitalize("kazuki")



###
### None is returned by functions by default
out = print("hello")
print(out)


###
### Roman numeral conversion

def numeral(number):
    if type(number) != int or number <= 0:
        print("Roman numerals undefined")
        return
    if number > 1999:
        print("Unsupported")
        return
    ## 
    result = ""
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    ## 
    for n in range(len(values)):
        while number >= values[n]:
            ## subtract the number
            number -= values[n]
            ## concatenate
            result += numerals[n]
    ## 
    assert number == 0, "There's something left over" # debug
    return result


numeral(0)
numeral(1)
numeral(3)
numeral(14)
numeral(150)
