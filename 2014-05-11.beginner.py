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
m = [1,2,3,4,5,6]
m[::-1] # reverse slicing
n = len(m) - 1
m_rev = []
while not n < 0:
    m_rev.append(m[n])
    print(m[n])
    n = n - 1
m_rev


## string
m = ["hello","catastrophic","north","salami","bison","east","tmesis","west","bifurcate","south"]
m

n = 0
while n < len(m):
    if m[n] in ["north","south","east","west"]:
        m[n] = "[CENSORED]"
    n = n + 1
print(m)



## problem 5
5 % 6
## integer division
24 // 10

s1 = [4,87,2,6,44,17]
s2 = [98,77,6,13,14]
result_list = []

n = 0
while n < len(s1):
    if s1[n] % 2 == 0:
        result_list.append(s1[n])
    n = n + 1
    
n = 0
while n < len(s2):
    if s2[n] % 2 == 0:
        result_list.append(s2[n])
    n = n + 1

result_list


## smarter
s3 = s1 + s2
n = 0
result_list = []
while n < len(s3):
    if s3[n] % 2 == 0:
        result_list.append(s3[n])
    n = n + 1
result_list

## by list comprehension
[x for x in s1 if x % 2 == 0] + [x for x in s2 if x%2 == 0]


## problem 6
wordA = input("Give me a word. ")
wordB = input("Give me another word. ")

result = wordA

if len(wordA + wordB) >= 30:
    result += '.' * (30 - len(wordA))
else:
    result += '.' * (30 - len(wordA + wordB))
    result += wordB
print(result)
