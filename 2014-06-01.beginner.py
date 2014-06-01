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

removeWhitespace("Kauki Yoshida")
