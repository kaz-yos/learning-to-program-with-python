### Set A:
# [uses variables, ints, strings, print(), input(), if/else]

# 1.	Ask the user for a number. Using if/elif/else, provide at least 4 possible output responses depending on the value of the number, such as “7 is my favorite number!”, “3 is good luck!”,”999 is really high!”, etc. There should be a response no matter what number is given.

my_number = int(input("Give an integer: "))

if my_number < 0:
    print("That is a negative numer")
elif my_number == 0:
    print("That is exactly zero")
elif my_number < 10:
    print("That is a single digit positive integer")
else:
    print("That is a positive integer with more than two digits")


# 2.	Ask the user for their birthday by asking for the year, then the month number, then the day number. Tell them how old they are in years, then how old they are in months, then how old they are in weeks, then in days. If they give you an invalid birthday, do not crash.
my_year  = int(input("What is your birth year in four digitis: "))
my_month = int(input("What is your birth month in number: "))
my_day   = int(input("What is your birth day number: "))

str_my_month = ("00" + str(my_month))[-2: ]
str_my_day   = ("00" + str(my_day))[-2: ]

my_ymd = str(my_year) + "-" + str_my_month + "-" + str_my_day

## Get current date
import time
print(time.strftime("%Y-%m-%d"))

## Date calculation
# http://stackoverflow.com/questions/151199/how-do-i-calculate-number-of-days-betwen-two-dates-using-python



# 3.	Ask the user for a number, a mathematical operator, and then another number. Print out the result of the operation. For example, if the user enters  3, *, 4, the program should print 12, which is the value of 3 times 4.

# 4.	Simulate a conversation by doing the following:

# a.	Print  a greeting.
# b.	Ask the user how they’re doing.
# c.	Depending what they say, give different responses and ask different questions. Make the conversation last at least 3 prompt/response intervals.

# 5.	Ask the user for a number. Tell them whether it is even or odd.
