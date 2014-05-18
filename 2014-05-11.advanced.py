### 2014-05-11 advanced

## tuples are immutable lists
myTuple = ()
type(myTuple)

a = (1,2,3)
b = (1,2,3)
a + b

## only refering to data
a.count(1)
a.index(1)


location = (4.23, 4.13)
name = "Julian Eden"
name.split()
name = ("Julian","Eden")
type(name)


x = ([1,2], [3,2])
x[0].append(3)
x
x.append(12)
x

x = 1,2,3
type(x)

a,b,c = x
a
b
c
[a,b,c]
x = (1,2,3,4)
a,b,c = x
a,b,c = "678"
[c,b,a]


a = b = c = [1,2,3]
a.append(12)
b


## swap
a = 1
b = 2
a,b = b,a       # tuple, unpacking really!
a,b


## sequence unpacking in loops
for x,y in [(1,"a"), (2,"b"), (3,"c")]:
    print(x,y)


## zip
first = [1,2,3]
second = ["a", "b", "c"]
zip(first, second)
list(zip(first, second))


## zip() with loops
a = [1,2,3]
b = [True,False,False]
for x,y in zip(a,b): # tuples created
    print(x,y)



## guilt-in functions as constructors
int()
float()
str()
list()
tuple()

## first is much faster
m = []
m = list()


## dictionaries
myDict = {"oneKey": 1, "otherKey": 3}
type(myDict)
len(myDict)
myDict[0]
myDict["oneKey"]
## adding
myDict[0] = "donkey"
myDict
myDict["names"] = ["joe","samantha","chrysanthemum"]
myDict
myDict["names"]
myDict["names"][0]
## with default
myDict.get("names", "default")
myDict.get("joe", "default")
myDict[0]
myDict[0] = "king"
myDict

cities = {"London": (3.14, 6.32),
          "Paris": (7.32, -23)}
cities
cities["London"]


m = {"cities": {"L": (1,2,3), "P": (2,4)},
     "name": "Test"}
m
m["cities"]
m["cities"]["L"]
m["cities"]["L"][1]
"cities" in m
"city" in m

## accessing elements
## keys only
m.keys()
## values only
m.values()
## key-value pairs as tuples
m.items()

accounts = {
    "4433": 4000,
    "0056": 2343,
    "2222": 85789985
}
input_PIN = "4433"
accounts[input_PIN]



### sets
s = {1,2,3,3}
## no duplication
s

## string
miss = set("mississippi")
miss

a = {1,2,3}
b = {2,3,4}
## in both
a & b
## in either
a|b
## xor (exclusive or)
a ^ b
## difference
a - b
b - a

