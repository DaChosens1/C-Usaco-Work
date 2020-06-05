fin = open('measurement.in')
#fin = open('ex.txt')
recordings = []
count = 1
for line in fin:
    if count != 1:
        line = line.strip()
        days, name, amount = line.split(' ')
        days = int(days)
        if "+" in amount:
            n, amount = amount.split('+')
        amount = int(amount)
        recordings.append([days, name, amount])
    else:
        line = line.strip()
    count += 1
fin.close()
recordings.sort()
b = 7
e = 7
m = 7
display = "bem"
new_display = "bem"
changes = 0
for record in recordings:
    if record[1] == "Bessie":
        b += record[2]
    elif record[1] == "Elsie":
        e += record[2]
    elif record[1] == "Mildred":
        m += record[2]
    max_num = max([b, e, m])
    new_display = ""
    if b == max_num:
        new_display += "b"
    if e == max_num:
        new_display += "e"
    if m == max_num:
        new_display += "m"
    if new_display == display:
        pass
    else:
        display = new_display
        changes += 1

#print(changes)

fout = open("measurement.out", "w")
fout.write("{}".format(changes))
fout.close()