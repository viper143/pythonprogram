smallest = 0
for i in range(3):
    number = int(input("enter an inteer"))
    if i == 0:
        smallest = number

    if number < smallest:
        smallest = number

print(smallest)