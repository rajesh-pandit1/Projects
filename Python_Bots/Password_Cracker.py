from random import *
import os

your_pwd=input("Enter your password: ")

pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

pw = ""

while(pw!=your_pwd):
    pw=""
    for letter in range(len(your_pwd)):
        guess_pwd=pwd[randint(0,17)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking Password..... Please wait")
        os.system("cls")

print("your password is:",pw)