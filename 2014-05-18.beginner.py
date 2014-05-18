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



