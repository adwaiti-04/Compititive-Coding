# WAP to if percentage is greater than 90 so assign grade A if the percentage greater than 80 assign grade B 
# if percentage is greater than 60 so assign grade C if the perecntage is below 60 so print "FAIL"

per = int(input("Enter Your percentage: "))

if per>=90:
    print("Grade A")

elif per>=80 and per<90:
    print ("Grade B")

elif per>=60 and per <80:
    print("Grade C")

else:
    print("FAIL!!")