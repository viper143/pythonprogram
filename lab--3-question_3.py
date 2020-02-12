limit = int(input("Enter your limit"))
for i in range(limit):
    if i % 2 == 0:
        print(str(i) + " Even")
    else:
        print(str(i) + " Odd")