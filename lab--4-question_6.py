numbers = []
oddCount = 0
evenCount = 0

for i in range(100):
    numbers.append(i)

for item in numbers:
    if item % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print(oddCount)
print(evenCount)
