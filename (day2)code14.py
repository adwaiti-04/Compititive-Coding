for i in range(1,11):
    print(i*2," ")
    

# TABLE OF 11, 12 and 4

for i in range(1,11):
    print(i*2," ",i*3," ",i*4)

print()

for i in range(1,11):
    print(i*11," ",i*12," ",i*4)

#CALCULATE THE RANGE

name = "adwaiti"
i = 0 #3
for x in name:
    if x == 'n':
        print("The character present at index no ",i,"value=",x)
        break
    i=i+1

# EXAMPLE
for i in range(10):
    if i ==5:
        continue
    print(i)