m1 = int(input("Enter phone number of person 1\n"))
m2 = int(input("Enter phone number of person 2\n"))
m3 = int(input("Enter phone number of person 3\n"))
m4 = int(input("Enter phone number of person 4\n"))

if(m1>m2 and m1>m3 and m1>m4):
    print("The greater number of the person is person1")
elif(m2>m1 and m2>m3 and m2>m4):
        print("The greater numbr of the person is person 2")
elif(m3>m1 and m3>m2 and m3>m4):
    print("The greater number of the person is person 3")
else:
    print("The greater number of the person is person 4")