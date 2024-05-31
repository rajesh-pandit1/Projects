mydict = {
    "fast": "In a quick manner",
    "Rajesh": "The coder",
    "marks" : "[1, 5, 5, 6,]",
    "anotherdict" : {"Rajesh" : 'Player'},
    1: 2,

}
# Printing the keys of the dictionary
print("The keys of the dictionary is :",mydict.keys())
# Printing the keys of the dictionary in a list
print("The keys of the dictionary in a list is : ",list(mydict.keys()))
print("All the content of the dictionary in a list is : ",list(mydict.items()))
updatedict = {"Naresh": "Brother",
"Bhagirath":"Father"}
mydict.update(updatedict)
print("The meaning of Naresh after updating is ",mydict)
print(type(mydict))