def show_star(count):
    star = ""
    for i in range(count + 1):
        star += "*"

    print(star)

for i in range(5):
    show_star(i)
for j in range(i - 1, -1, -1):
    show_star(j)
