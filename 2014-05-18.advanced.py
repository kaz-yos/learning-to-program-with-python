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
    def shout_name(self):
        print("MY NAME IS " + self.name.upper() + "!!!")

bill = Person()
bill.add_info("William Worthington III", 32, "pilot")
bill.profession
bill.shout_name()
