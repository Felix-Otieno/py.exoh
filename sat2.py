#An argument is a value send to the function when it is called.
#Function argument with default values

def addNumbers(a=7, b=8):
    sum = a + b
    print("sum:", sum)
addNumbers(2, 3)
addNumbers(2)
addNumbers()