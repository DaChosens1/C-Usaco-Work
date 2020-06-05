def min_list(list_use):
    min_value = [9999, 9999]
    for n in list_use:
        if n[0] < min_value[0]:
            min_value = n
    return min_value

fin = open('blist.in')
cows = []
count=1
for line in fin:
    line = line.strip()
    if count > 1:
        start, finish, amount = line.split(' ')
        cows.append([int(start), int(amount)])
        cows.append([int(finish), int(amount)*-1])
    count+=1
fin.close()
new_cows=[]
while len(cows)!=0:
    new_cows.append(min_list(cows))
    cows.remove(min_list(cows))
max_value=0
value=0
for i in new_cows:
    value+=i[1]
    if value>max_value:
        max_value=value
fout = open("blist.out", "w")
fout.write("{}".format(max_value))
fout.close()
