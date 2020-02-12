DISTINCTION = 70
FIRST_DIVISION = 60
PASS = 40

total = 0
percentage = 0
for i in range(3):
    total += float(input("Enter your marks"))

print("Total marks: " + str(total))
print("Percentage: " + str(total / 3))

if percentage >= DISTINCTION:
    print("Distinction")
elif percentage >= 60 and percentage < 70:
    print("First Division")
elif percentage >= 40 and percentage < 60:
    print("Pass")
elif percentage < 40:
    print("Fail")