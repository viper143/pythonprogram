dict =	{
  "1": 1,
  "2": 2,
  "3": 3
}

keys =  dict.keys()

for item in keys:
    if item == '4':
        print("key exists")
        break
    else:
        print("key doesn't exist")
