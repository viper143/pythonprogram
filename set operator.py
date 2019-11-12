#create a 3 sets for fruits, with random items, now, i need to get data how many items among the sets are repeated, how
#many of them are unique, in total get all the unrepeated items,

A={'apple','orange','grapes','pineapple'}
B={'grapes','apple','pomogranet','banana'}
C={'watermelon','orange','banana','guava'}
D=A.union(B).union(C)
print(D,'all the unrepeated items')
E=A.intersection(B).intersection(C)
print(E,'all the repeated items')
F=D.difference(E)
print(F,'the unique items')
