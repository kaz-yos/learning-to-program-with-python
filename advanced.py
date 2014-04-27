### Advanced session
## OOP in Python

## Inheritance syntax
class Template(ParentClassName):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def getArg1(self):
        return self.arg1


## Parent class
class Monster:
    counter = 0 # belongs to the class
    def __init__(self):
        Monster.counter += 1    # constructor call will add one
        self.health = 100       # belongs to the instances
        self.attack = 20
        self.defence = 20
        self.speed = 10
        self.accuracy = 0.50
        self.magic_resist = 0.30
        self.x = 0
        self.y = 0
    def move(self, x, y):
        self.x  += x
        self.y  += y

myMonster = Monster()
myMonster2 = Monster()
Monster.counter
Monster.health

class Undead(Monster):
    def __init__(self):
        super.__init__()        # set defaults
        self.undead = True
        self.bloodsuckingPower = 25
        
class Zombie(Undead):
    def __init__(self): 
        super().__init__() # undead constructro
        self.speed = 1

## polymorphism
myZombie = Zombie()
        

myMonster.counter = 20  # instance data created

Monster.counter = 20    # can overwrite
Monster.counter


        
## Empty new subclass
class Banshee(Monster):
    pass
            
my_first_banshee = Banshee()
type(my_first_banshee)
my_first_banshee.attack # Inherited from the parent

## Different
class Banshee(Monster):
    def __init__(self):
        # super().__init__()      # parent class's __init__
        self.attack = 25
        self.defence = 10
        self.accuracy = 1
my_first_banshee = Banshee()
type(my_first_banshee)
my_first_banshee.attack # Redefined
my_first_banshee.health # Needs inheritance


class Dragon(Monster):
    def __init__(self):
        ## Monster.__init__(self)
        super().__init__()      #  set defaults
        self.attack = 200       # overwrite
        self.defense = 200
        self.health = 1000
    def move(self, x, y):
        super().move(4 * x, 4 * y)      # change in argument to the prev func
        # self.x += 4 * x
        # self.y += 4 * y
    def flyAcrossContinent(self):
        self.move(3000,0)               # Child class 
        # super().self.move(3000,0)
        
dragon = Dragon()
dragon.attack
dragon.speed
dragon.x, dragon.y
dragon.move(3,4)
dragon.x, dragon.y


class Template(ParentClass):
    def __init__(self):
        super.__init__()        # set defaults
        self.arg1 = arg1        # overwrite
        self.arg2 = arg2
        
myMonster = Monster()
type(myMonster)
