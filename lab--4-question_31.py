set = {1, 2, 3}

for item in set:
    if item == 2:
        set.remove(item)
        break
print(set)