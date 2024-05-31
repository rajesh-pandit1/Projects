# creating an empty set
b = set()
print(type(b))


b.add(4)
b.add(9)
b.add(6)
b.add(5)
b.add(5) # Adding a value repeatedly doesn't changes a set
b.add((4, 5, 8, 9, 2,)) 
# b.add({4:5}) # cannot add list or dictionary to the set
print(b)
b.remove(5)
print(b)
print(len(b))
print(b.pop())