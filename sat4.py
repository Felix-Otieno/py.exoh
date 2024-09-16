#Python Function With Arbitrary Arguments
#Arbitrary arguments allow us to pass a varying number of values during a function call.
#We use an asterisk (*) before the parameter name to denote this kind of argument.

#Program to find sum of multiple numbers

def findSum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("sum =", result)
findSum(4, 5, 6)


def fullName(firstName, lastName):
    name = firstName+ " "+lastName
    return name
print(fullName("John", "Doe"))

def addAll(*numbers):
    return sum(numbers)
print(addAll(1, 2, 3, 4))

def is_prime(n):
    # Check if number is less than or equal to 1
    if n <= 1:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True