math = int(input("Enter your math's total marks in percentage\n"))
eng = int(input("Enter your english's total marks in percentage\n"))
scn = int(input("Enter your science's total marks in percentage\n"))
a = (math + eng + scn)/3
if (math<33 or eng<33 or scn<33):
    print("You are failed due to less marks in a subject")
elif(a<40):
    print("You are failed because of total marks is less than 40%")
else:
    print("Congratulation! You are passed")
