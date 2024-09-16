#Function is a code that is executed when is called from somewhere in a program.
#Parameters are information passed to a function.
#Arguments are values send to the function when it is called.
#Return statement states a specific value the print should output.

minMarks = 30
studentsMarks = float(input("Enter your marks:"))
if studentsMarks >= minMarks:
    print("You are eligible")
elif studentsMarks >= 25:
    print("You are almost there")
else:
    print("You are not eligible")