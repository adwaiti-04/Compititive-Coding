mylist = [] # [10, 11, 7, 12, 14]
sum = 0 # 1
N = int (input("Enter the value of N : "))
for i in range (N):
    val = int(input("Enter the value"))
    mylist.append(val)

for j in range (len(mylist)): # j=1 = 11-7 = 4
    if j+1 in range(len(mylist)): # 2<5
        sum += abs (mylist[j] - mylist[j+1])
        print(sum)