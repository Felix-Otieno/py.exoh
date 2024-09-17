def wages(hours):
    if hours <= 5:
       return hours * 15
    else:
        return 5 * 15 + (hours - 5) * 17
print(wages(4))
print(wages(6))