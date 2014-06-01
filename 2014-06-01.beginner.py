### 2014-06-01 beginner class


def addAllNumbers(*args):
    print(type(args))
    _sum = 0
    for n in args:
        _sum += n
    return _sum

addAllNumbers(3,4,5,6)


def removeWhitespace(string):
    result = ""
    for char in string:
        if char not in " \t\n": # space, tab, newline
            result += char
    return result

len("b")
len("\n")
len("\\")
len("\\n") # regular n

print(removeWhitespace("Kauki Yoshida is at a Python meetup."))


def printTriangle(base=50):
    m = 1
    while base >= 0:
        space = ' '*int(base/2)
        Xs = 'X' * m
        print(space + Xs + space)
        base -= 2
        m += 2

printTriangle()
printTriangle(30)

