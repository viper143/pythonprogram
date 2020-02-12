items = [1,3,4,55,1,22]

min = 0

for i in range(len(items)):
    if i == 0:
        min = items[i]

    if items[i] < min:
        min = items[i]

print(min)