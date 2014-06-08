### 2014-06-08

# class ChildClassName(ParentClassName):
#     def __init__(self):
#         # and so on .. nothing else change here.

## Inherit from the object class (prototype of all objects)
class Monster(object):
    def __init__(self):
        self.health       = 100
        self.attack       = 20
        self.defense      = 20
        self.speed        = 10
        self.accuracy     = 0.5
        self.magic_resist = 0.3


## Inheritance
class Banshee(Monster):
    ## Overwrite the default __init__j
    def __init__(self):
        ## Monster's __init__ method is invoked
        super().__init__()
        ## Override these values
        self.attack       = 25
        self.defense      = 10
        self.accuracy     = 1
        self.magic_resist = 0.0
        self.volume       = 50

class Dragon(Monster):
    def __init__(self):
        super().__init__()
        self.attack  = 200
        self.defense = 200
        self.health  = 1000


##
m = Monster()
b = Banshee()
d = Dragon()

## george is an instance of Banshee of course
isinstance(george, Banshee)
## it also inherited from the Monster class
isinstance(george, Monster)
