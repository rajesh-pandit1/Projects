story = "once upon a time there was a person whose name is Rajesh Pandit and was a good guy"

#string function
#printing total number of character in the story including space
print(" The total number of the character including space is ",len(story)) 
# checking the last word in true or false
print("Is the last word guy:",story.endswith("guy")) 
# checking the last word in true or false
print("Is the last word man:",story.endswith("man"))
# counting letter "o" in the story 
print("The number of (small) letter 'o' is:",story.count("o"))
print("The number of capital letter 'R' is:",story.count("R"))
print("Capitalizing first letter of the story:",story.capitalize())
#Finding the position of a word
print("The position of the word 'Rajesh' is ",story.find("Rajesh"))
#Replacing words
print("After replacing: ",story.replace("Rajesh","Naresh"))