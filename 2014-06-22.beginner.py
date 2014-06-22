### 2014-06-22 Beginner
## File I/O

## open() function 2 args
## file and mode
## open("example.txt", "r+")
## r read
## w write
## a append
## + read and write
## http://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r
## stream is where the cursor is
## w delete a current file
## w+ reading and writing
## stream at beginning of file: r/w
## stream at end of file: a
## r+ does not create a file if it does not create

## operating system module
import os
print(os.getcwd())
## this is where the file is looked for in or created in

## read a file (existing one only)
## defaults to r (reading only)
with open("example.txt", "r+") as f:
    
    type(f)

## file methods
## f.read() entire content of the file
## f.readline() next line of the file
## f.readlines() list of strings (each string represents a line)
# print(f.readlines())

## seek method
## f.seek(22,0)
## at the end of file
## f.seek(0, 2)

## f.tell()
## how many characters into the file before the cursor

# ## write to the file
# f.seek(30,0)
# ## return value is the number of characters written
# f.write("HELLO")
# ## to insert instead of overwrite

    content = f.readlines()
    print(content)

    content[0] += "TESTING"
    finalText = "".join(content)

    f.seek(0,0)
    print(f.write(finalText))


## close a file
## no need to close 
# f.close()


## 
with open("helloworld.py", "w") as f:
    f.write("print('hello world')\n")
    f.write("input()")
