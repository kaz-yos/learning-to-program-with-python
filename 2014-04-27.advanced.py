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
