# Important: This syntax will create an empty dictionary not an empty set
a = {}
print(type(a))

# An empty set can be created using the below syntax:
b = set()
print(type(b))
# Adding numbers in the empty set
b.add(4)
b.add(5)
print("After adding : ",b)