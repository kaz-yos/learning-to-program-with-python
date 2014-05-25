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
