### 2014-05-18 Advanced

n = []
if n:
    print("empty")

## class definition
class Person:
    def add_info(self, name, age):
        self.name = name # attributes
        self.age  = age  #

class Person:
    def add_info(self, name1, age1):
        self.name = name1 # attributes
        self.age  = age1


m = 6
type(m)


## method invocation on an instance of a list class
m = [1,2,3,4]
m.reverse()
m

len([2,3,4])
## JS m.length #  sttribute

## Create an instance
test_person = Person()
## Method invocation
test_person.add_info("Bill",36)
## Direct access to attributes
test_person.name
test_person.age

## Instances are separate things
joe = Person()
diana = Person()
joe.add_info("Joseph Mariano", 12)
diana.add_info("Diana Corduroy", 78)

## can create a new slot
diana.hello = 3
diana.hello

jim = Person()
jim.add_info("James Smith", 25)
jim.name
jim.age
jim.profession
## Attributes are public
jim.profession = "created on the fly"
jim.profession

## 
class Person:
    def add_info(self, name, age, profession):
        self.name = name # attributes
        self.age  = age
        self.profession = profession
        ## 
    def shout_name(self):
        print("MY NAME IS " + self.name.upper() + "!!!")
        ## 
    def is_a_teenager(self):
        return 12 < self.age < 20

bill = Person()
bill.add_info("William Worthington III", 32, "pilot")
bill.profession
bill.shout_name()

bill.is_a_teenager()

## 
class Person:
    ## Python instanciate using __init__ method automatically.
    def __init__(self, name, age):
        self.name = name # attributes
        self.age  = age

## default
class Person:
    ## Python instanciate using __init__ method automatically.
    def __init__(self, name = "Default", age = 0):
        self.name = name # attributes
        self.age  = age

        
sam = Person("Samantha", 17)
sam.name
sam.age

sam2 = Person()
sam2.name
sam2.age



## one more example

class Rectangle:
    def __init__(self, w, h):
        self.width     = w
        self.height    = h
        self.area      = w * h
        self.perimeter = 2 * (w + h)
    def is_square(self):
        return self.width == self.height


m = Rectangle(3,4)
n = Rectangle(7,7)
rec_list = []
rec_list.append(m)
rec_list.append(n)
rec_list[0].is_square()
rec_list[1].is_square()
    
