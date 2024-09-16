#Default arguments in function
#Default arguments are used when no explicit values are passed to these parameters during a function call.

def greet(name, message="Hallo"):
    print(message,name)
greet("Alice", "Good Morning")
greet("Bob")