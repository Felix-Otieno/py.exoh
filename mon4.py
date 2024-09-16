list = [8, 3, 1, 4]
length = len(list)
for i in range(length):
    for j in range(0, length-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)       