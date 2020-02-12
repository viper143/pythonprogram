data = "HelloWorld"

length = len(data) - 1
lowerCase = 0
upperCase = 0
while (length>= 0):
    if data[length].isupper():
        upperCase += 1
    else:
        lowerCase += 1

    length = length - 1

print(lowerCase)
print(upperCase)