# WAP to perform arithematic operation using functional programming approach
# Functions helps us to achieve modularity approach

import sys

def addition(num1, num2): #called function
    print("Addition=", num1 + num2)

def subtraction(num1, num2): #called function
    print("Subtraction=", num1 - num2)

def multiplication(num1, num2): #called function
    print("Multiplication=", num1 * num2)

def division(num1, num2): #called function
    print("Division=", num1 / num2)
    pass

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice from above options : "))
    if choice == 5:
        sys.exit()
    val1 = int(input("Enter Frist Value : "))
    val2 = int(input("Enter Second Value : "))
    if choice == 1:
        addition(val1 , val2)
    elif choice == 2:
        subtraction(val1, val2)
    elif choice == 3:
        multiplication(val1, val2)
    elif choice == 4:
        division(val1, val2)
        pass
    else:
        print("You have enntered the wrong choice")
