### 2014-05-11 Learning to program with Python
## Lists

## Create an empty list
myList = []
myList

myList = ["h", True, 4, 6, "string"]
myList

## Lists are dynamic containers
myList = []
len(myList)

myList = [1, "a", 6]
len(myList)
myList.append("hi")
myList

myList = [1,2,3]
myList
myList.count(1)

myList.pop()
myList
myList.pop()
myList
myList.pop()
myList


myList = [5,1,2,3,4]
myList
myList.sort()
myList


m = [1,2,3,4,5]
type(m)


m = [4,9,3,7,2]
m[0]
m[1]
m[5]


m[1] = 10
m

m[0:2] = [3,5]
m
a = 2
m[0:a]


"hello"[0:-1]


## looping through lists
m = [1,2,3,4]
n = 0
while n < len(m):
    print(m[n])
    n = n + 1



## 1 
m = [1,23,6,0.1]
result_list = []
n = 0

while n < len(m):
    if type(m[n]) == int:
        result_list.append(m[n] * 2)
    else:
        result_list.append(m[n])
    n += 1
print(result_list)


[2 * x for x in m if type(x) == ]


## problem 2

m = [4,7,3,2,"hi"]
sum(m)

n = 0
acc = 0
while n < len(m):
    if type(m[n]) == int:
        acc = acc + m[n]
    n += 1
acc

type(4) == int
type(4) == int


## problem 3
