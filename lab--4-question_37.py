number = 15
dictionary = dict()
for i in range(number):
    key = i + 1
    dictionary.update({ str(key): key * key})

print(dictionary)
