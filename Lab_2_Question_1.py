naturalNumber = []

for i in range(5):
    naturalNumber.append(i + 1)

def doesExist(number, arrayList):
    for item in arrayList:
        if number == item:
            return True
    return False

print(doesExist(5, naturalNumber))