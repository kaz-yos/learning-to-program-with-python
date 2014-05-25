### Set A:
# [uses variables, ints, strings, print(), input(), if/else]

### 1.	Ask the user for a number. Using if/elif/else, provide at least 4 possible output responses depending on the value of the number, such as “7 is my favorite number!”, “3 is good luck!”,”999 is really high!”, etc. There should be a response no matter what number is given.

my_number = int(input("Give an integer: "))

if my_number < 0:
    print("That is a negative numer")
elif my_number == 0:
    print("That is exactly zero")
elif my_number < 10:
    print("That is a single digit positive integer")
else:
    print("That is a positive integer with more than two digits")


### 2.	Ask the user for their birthday by asking for the year, then the month number, then the day number. Tell them how old they are in years, then how old they are in months, then how old they are in weeks, then in days. If they give you an invalid birthday, do not crash.
my_year  = int(input("What is your birth year in four digitis: "))
my_month = int(input("What is your birth month in number: "))
my_day   = int(input("What is your birth day number: "))

## Last two characters
## http://www.daniweb.com/software-development/python/threads/354502/how-do-i-get-the-last-two-character-in-a-string
str_my_month = ("00" + str(my_month))[-2: ]
str_my_day   = ("00" + str(my_day))[-2: ]

## yyyy-mm-dd format string
my_ymd = str(my_year) + "-" + str_my_month + "-" + str_my_day

## Get current date
import time
date_fmt = "%Y-%m-%d"
current_date = time.strftime(date_fmt)
print(current_date)

## Date calculation
# http://stackoverflow.com/questions/151199/how-do-i-calculate-number-of-days-betwen-two-dates-using-python

import datetime
current_date_obj = datetime.datetime.strptime(current_date, date_fmt)
birth_date_obj = datetime.datetime.strptime(my_ymd, date_fmt)

delta_date_in_days = current_date_obj - birth_date_obj

## Tell in years
year_difference = int(time.strftime("%Y")) - my_year
## datetime object for the birthday this year
birth_day_this_year = time.strftime("%Y") + "-" + str_my_month + "-" + str_my_day
birth_day_this_year_obj = datetime.datetime.strptime(birth_day_this_year, date_fmt)
## datetime object for the current date
current_date_obj = datetime.datetime.strptime(current_date, date_fmt)

## Compare the current
if current_date_obj >= birth_day_this_year_obj:
    print("you are " + str(year_difference) + " years old.")
else:
    print("you are " + str(year_difference - 1) + " years old.")

## Tell in months
print("you are " + str(int(delta_date_in_days.days / 30)) + " months old")

## Tell in weeks
print("you are " + str(int(delta_date_in_days.days / 7)) + " weeks old")

## Tell in days
print("you are " + str(int(delta_date_in_days.days)) + " days old")



### 3.	Ask the user for a number, a mathematical operator, and then another number. Print out the result of the operation. For example, if the user enters  3, *, 4, the program should print 12, which is the value of 3 times 4.

## ask for three things separated by ,
# http://stackoverflow.com/questions/14444512/how-do-you-create-multiple-variables-from-raw-input-in-python
user_input = input("Give number a, an operator, and number b separated by ,: ")
user_input_split = user_input.split(",")
a = user_input_split[0]
opr = user_input_split[1]
b = user_input_split[2]
ans = eval(a + opr + b)
print("The ans is " + str(ans))


### 4.	Simulate a conversation by doing the following:
# a.	Print  a greeting.
# b.	Ask the user how they’re doing.
# c.	Depending what they say, give different responses and ask different questions. Make the conversation last at least 3 prompt/response intervals.


### 5.	Ask the user for a number. Tell them whether it is even or odd.
my_number = int(input("Give an integer"))
if (my_number % 2) == 0:
    print("even")
else:
    print("odd")


###
### Set B
# [uses looping]
### 1.	Print out the entirety of the lyrics to the song “99 Bottles of Beer on the Wall.”
## use for after spliting a string at spaces

### 2.	Create a guess-the-number game. Pick a number, then ask the user for a guess. If their guess is low, tell them “Higher!” and ask for another guess. If their guess is high, tell them “Lower!” and ask for another guess. If their guess is correct, tell them “You got it!” and end the loop.

### 3.	Without looking, replicate what I did in class and print out a triangle of X’s, then a diamond.

### 4.	Find all prime numbers lower than 1000.
# A prime number is a number that cannot be evenly divided by anything besides itself and 1.
# 11 is a prime number, as is 5, 3, 2, 17, etc.
# 10 is not a prime number, because it is divisible by 5 and 2.
# Remember that the modulus operator (%) tells you what’s left over after a division operation. 5 % 2 is 1, because 2 goes into 5 twice with 1 left over.

candidates = range(2, 1000 + 1)

## just print them all
for i in candidates:
    print(str(i))

## for and print solution
for i in candidates:
    ## Create a list of values lower than i
    divisor_candidates = filter(lambda x: x < i, candidates)
    ## Keep ones with reminder zero
    good_divisors      = filter(lambda x: (i % x) == 0, divisor_candidates)
    ## if nothing left, a prime
    if len(list(good_divisors)) == 0:
        print(str(i) + " is a prime.")


## More functional solution
def is_prime(x):
    divisor_candidates = range(2,x)
    good_divisors      = filter(lambda y: (x % y) == 0, divisor_candidates)
    return len(list(good_divisors)) == 0
is_prime(2)
is_prime(3)
is_prime(4)
## Filter elements in candidates, using the is_prime(x) function
list(filter(lambda x: is_prime(x), candidates))



### 5.	Iteratively print the first 25 numbers of the Fibonacci sequence. The first two terms are 0 and 1. From there, each successive term is the sum of the two previous terms.

## Recursive function
def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

## Function to print
def fibonacci_print(x):
    for i in map(fib, range(0,x)):
        print(i)

fibonacci_print(25)


###
### Set C:
# [uses functions, lists, and string methods]

### 1.	Write a recursive function which returns a list containing the first N terms of the Fibonacci sequence. Warning: this is tricky.

## Function to print
def fibonacci_list(x):
    return list(map(fib, range(0,x)))

fibonacci_list(1)
fibonacci_list(25)



### 2.	Create a function which, when run, simulates a console version of Connect 4. The Connect 4 board is a 7x6 grid, best represented as a list of lists, also known as a matrix. The game would run a loop where each iteration is a new turn. This would be time-consuming, but not too tricky.

# Each turn should involve the following:
# a.	The current state of the Connect 4 grid should be printed out.
# b.	A message should be printed saying which player’s turn it is.
# c.	It should then wait for the player to select a column, and place their color square at the lowest unfilled spot of that column.
# d.	It should then check whether the player has won, and either ask if they want to start a new game, or else proceed to the next turn if the game is not yet over.



### 3.	Write a recursive implementation of QuickSort.


### 4.	Write a function which takes a paragraph of text (as a string) and returns a new  string with the following changes made:

# a.	All periods changed to exclamation points.
# b.	All words containing a “q” replaced with “[CENSORED]”
# c.	All capitalized words prefaced by “Mr.” or “Mrs.”

### 5.	Write out your own versions of the following Python built-ins:
# a.	max()   #takes a list, returns highest value
# b.	min()   #takes a list, returns lowest value
# c.	len()    #takes a list, returns the length of the list
# d.	sum()  #takes a list, returns sum of values
# e.	reversed()   #takes a list, returns a reversed list
# f.	map()  #takes a list and a function and returns a new list constructed by applying the function to each value in the original list
# g.	filter()  #takes a list and a function and returns a new list constructed by applying the function to each value in the original list to see whether the funciton returns True or False. The new list only contains those values for which the function returned True.

