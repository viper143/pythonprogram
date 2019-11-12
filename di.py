#add key and value to existing dictionary
d = {'no1':10, 'no2':20}
d2 = {'no3':30, 'no4':40}
d.update(d2)
print(d)

#concatinate multiple dictionaries
dict1 = {'no1':10, 'no2':20}
dict2 = {'no3':10, 'no4':20}
dict4 ={}
for d in (dict1, dict2):dict4.update(d)
print(dict4)

#check weather key is present or not

d = {'john':41,'sam':87}
if 'john' in d:
    print('key is present')
else:
    print('key is not present')