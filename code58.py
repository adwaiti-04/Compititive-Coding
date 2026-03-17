list = [0, 1, 2, 5, 6]

for i in list:
    if i == 0:
        list.remove(i)
        list.append(i)
print(list)