mydict = {
    "fast": "In a quick manner",
    "Rajesh": "The coder",
    "marks" : "[1, 5, 5, 6,]",
    "anotherdict" : {"Rajesh" : 'Player'}
}
# Changing the value of marks
mydict['marks']=[78, 256, 56]
print("Ther meaning of Fast is ",mydict["fast"])
print("The meaning of Rajesh is ",mydict["Rajesh"])
print("The meaning of marks is ",mydict["marks"])
print("The meaning of Rajesh in another dictionary is ",mydict["anotherdict"]['Rajesh'])