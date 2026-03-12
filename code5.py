# WAP to accept three number and check maximum number and print 

n1 = int(input("Enter first no: "))
n2 = int(input("Enter second no: "))
n3 = int(input("Enter third no: "))

if n1 > n2 and n1 > n3:
    print("n1 is max")
elif n2 > n1 and n2 > n3:
    print("n2 is max")
else:
    print("n3 is max")