name = 'Adwaiti*is*a*good*programmer'
newname = '' # empty str | Adwaiti
val = ''  # empty str | *
for i in name: # i= 7:
    if i != '*':
        newname += i
    else:
        val += i
print(newname)
print(str(val+newname))