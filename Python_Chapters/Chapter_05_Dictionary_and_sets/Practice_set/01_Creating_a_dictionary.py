dict = {"mango" : "Aam",
"apple" : "Sheb",
"grapes" : "Angur",
"Gauva" : "Amrud",}
print("The options are",list(dict.keys()))
a = input("Enter the word in English : ")
print("The meaning in hindi is ",dict.get(a))