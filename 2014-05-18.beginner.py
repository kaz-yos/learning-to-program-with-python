### 2014-05-18 Python meetup beginner


0.11 * 9



### loops

##  while
m = ['a', 'b', 'c']
n = 0
while n < len(m):
    print(m[n])
    n = n + 1

## for over a iterative data
for x in "hello":
    print(x)

## conditional printing
m = [1, "hi", True, 4.0]
for item in m:
    if type(item) == str:
        print(item)

## while
while n <= 10:
    print(n)
    n = n + 1

## for easier
for n in range(10 + 1):
    print(n)

## breaking out
for n in range(10):
    print(n)
    if n == 4:
        break

## Skipping
for n in range(10):
    if n == 2:
        continue
    print(n)

## no overwrite (copying element n)
myList = [1,2,3,4]
for n in myList:
    n = 5

## no change
myList

for n in range(len(myList)):
    print(myList[n])
    myList[n] = 5
## change now
myList


## realize range object
type(range(200))
myList = list(range(200))
myList



### Functions
def add(x,y):
    return x + y
add(4,5)

def multiply(x,y):
    return x * y

def subtract(x,y):
    return x - y

add(4,4) + subtract(2,9) * multiply(7,2)


##
def doesWordHaveVowels(word):
    for letter in word:
        print(letter)
        if letter in "aeiou":
            return True
    return False # identation at the same level as for (outside for loop)

doesWordHaveVowels("kazuki")
doesWordHaveVowels("kzk")

## multiple return statements
def searchTwoListsForAWord(listA, listB, word):
    for x in listA:
        if x == word:
            print("found it in listA!")
            return True
    ##
    for x in listB:
        if x == word:
            print("found it in listB!")
            return True
    ##
    print("did not find the word")
    return False


##
def combineListOfString(strings):
    result = ""
    for s in strings:
        result = result + s
    return result
combineListOfString(["aa","bb","cc"])
