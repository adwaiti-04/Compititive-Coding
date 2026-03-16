def login():
    username = input("Enter username :")
    password = input("Enter password :")
    if username == password:
        print("Logged in succesfully")
    else:
        print("Invalid credentials")

login()
print("THANK YOU!!")