set1 = {1,2,3}
set2 = {1, 2, 3, 4}
print(len(set1))
set1.add(10)
print(set1)
set1.remove(10)
print(set1)
set1.discard(5)
print(set1)

print("------------")
print(set1 == set2)
print(set1 <= set2)#set1.issubset(set2)
print(set1 >= set2)#set1.issuperset(set2)

print("------------")
set1 = {2, 3, 4}
set2 = {1, 2, 3}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

print("------------")

set1 = {1, 3, 5, 7, 9, 10}
set2 = {2, 4, 6, 7, 8, 9, 1}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))