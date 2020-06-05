fin = open('sleepy.in')
#fin = open('mixmilk.txt')
count = 1
for line in fin:
    if count!=1:
        line = line.strip()
        position = list(line.split(' ')).copy()
        starting_pos=list(map(lambda x: int(x), position))
    else:
        line=line.strip()
        total = int(line)
    count+=1
fin.close()
counter = 0
total-=1
pos=starting_pos.copy()
sorting_pos=pos[::-1]
for i in range(len(sorting_pos)-1):
    if sorting_pos[i]>sorting_pos[i+1]:
        total-=1
    else:
        break
#print(total)
fout = open("sleepy.out", "w")
fout.write("{}".format(total))
fout.close()
