ch = ord(input("Enter any character"))
# ord function is used to convert in ascii code
if ch>65 and ch<=91:
    print("Your entered character in upper case")
elif ch>=97 and ch<=122:
    print("Your entered character is in lower case")
elif ch>=48 and ch<=57:
    print("Your entered charactervis in digit")
else:
    print("Your entered characteris in special symbol") 
    