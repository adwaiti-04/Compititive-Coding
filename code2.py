# WAP to accept days and check working days and weekend 

day = input("Enter your day:")

if day == "SATURDAY " or day =="SUNDAY" or day =="saturday" or day=="sunday" or day =="Saturday" or day =="Sundays":
    print("It's weekend")

else:
    print("Working day")