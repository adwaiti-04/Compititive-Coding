# TYPES OF ARGUMENTS
# ~ Positional argument 
# ~ Keyword arguemnt 
# ~ Default arguemnt
# ~ Variable argument
# ~ 


# POSITIONAL ARGUEMNT 
def personalInfo(fname, lname):
    print("First name:", fname)
    print("Last name:", lname)
personalInfo("Adwaiti","Kankale")

# KEYWORD ARGUMENT
def personalInfo(fname, lname):
    print("First name:", fname)
    print("Last name:", lname)

fname = "Adwaiti"
lname = "Kankale"
personalInfo(fname, lname)

# DEFAULT ARGUMENT
def cityName(city = "NAGPUR"):
    print("City Name", city)

cityName("Mumbai")
cityName("Delhi")
cityName()