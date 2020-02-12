STARTING_NUMBER = 1500
ENDING_NUMBER = 2700

index = STARTING_NUMBER

while index <= ENDING_NUMBER:
    if index % 7 == 0 and index % 5 == 0:
        print(index)
    index += 1