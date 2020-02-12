def show_stars(rows):
    stars = ""
    for i in range(rows+1):
        stars += "*"
    print(stars)

for i in range(5):
    show_stars(i)
