mylist = [2,5,8,4,1,9,8]
even = 0 #1
odd = 0 #1
for i in mylist: #i-1
    if i%2 == 0:
        even += 1
    else:
        odd =+ 1

print("Even=", even)
print("Odd=", odd)