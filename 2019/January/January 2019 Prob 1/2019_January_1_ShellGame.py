def swap(swap_list, index_1, index_2):
    a, b = index_1, index_2
    swap_list[b], swap_list[a] = swap_list[a], swap_list[b]
fin = open('shell.in')
count = 1
swaps=[]
times=0
for line in fin:
    if count!=1:
        line = line.strip()
        a, b, g = line.split(' ')
        swaps.append(list(map(lambda x: int(x), [a, b, g])))
    else:
        times=int(line.split(' ')[0])
    count+=1
fin.close()
one=False
two=False
three=False
shells=[one, two, three]
max_point=0
point=0
for i in range(3):
    if i == 0:
        one = True
    elif i == 1:
        two = True
    elif i == 2:
        three = True
    shells=[one, two, three]
    for num in range(times):
        swap(shells, (swaps[num][0])-1, (swaps[num][1])-1)
        if shells[((swaps[num][2])-1)]:
            point+=1
            
    if point > max_point:
        max_point = point
    point=0
    one=False
    two=False
    three=False
fout = open("shell.out", "w")
fout.write("{}".format(max_point))
fout.close()

