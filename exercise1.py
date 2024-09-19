previousNum = 0
for i in range(1, 11):
    total = previousNum + i
    print("Current Number", i, "Previous Number ", previousNum, " Sum: ", total)
    previousNum = i