# WAP to accept three papaer marks and calculate total marks, percentage an check if percentage is greater than or 
#  greater then or equal to 60 then he/she is eligible for placement.

phy = int(input("Enter the marks of Physics :"))
math = int(input("Enter the marks of Maths :"))
chem = int(input("Enter the marks of chem :"))

total = phy+math+chem
percentage = total/3
print("Total=", total)
print("percentage =", percentage)

if percentage >= 60:
    print("you are eligible for placement")
else:
    print("you aren't eligible for the placement")