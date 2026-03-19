#nested function

def outerfunction():
    print("this is my outer function :")#second

def innerfunction():
    print("inner Function")
    innerfunction()#third
outerfunction()# first exe start from here