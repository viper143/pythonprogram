def reverse(string):
    reversedString = ""
    index = len(string)
    while index > 0:
        reversedString += string[index - 1]
        index = index - 1
    return reversedString

data = ["Hello", "madam"]
for item in data:
    if item == reverse(item):
        print(str(item) + " is palindrome")
    else:
        print(str(item) + " is not palindrome")