userInput = input("Enter a string")
length = len(userInput)
index = 0
while(index < length):
    if index % 2 == 0:
        print(userInput[index])

    index += 1