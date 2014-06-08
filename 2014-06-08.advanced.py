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
    pass


## 
barry = Monster()
george = Banshee()


## george is an instance of Banshee of course
isinstance(george, Banshee)
## it also inherited from the Monster class
isinstance(george, Monster)
