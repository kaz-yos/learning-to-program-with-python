## Message
print("This stuff module just started executing")

## Define variables
number = 5
age    = 10
rate   = 15

## Define a function
def capitalizeWords(string):
    words = string.split()
    result = []
    for w in words:
        result.append(w.title())
    return " ".join(result)

## Message
print("This stuff module just finished executing")
