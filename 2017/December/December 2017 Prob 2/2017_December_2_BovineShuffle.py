def findsort(dictionary, in_list):
    out_list = in_list.copy()
    for n in range(len(in_list)):
        out_list[n] = dictionary[out_list[n]]
    return out_list


fin = open('shuffle.in')
observations = []
movement = []
count = 1
for line in fin:
    if count == 2:
        line = line.strip()
        movement = list(map(lambda x: int(x), line.split(" ")))
    elif count == 3:
        line = line.strip()
        observations = list(map(lambda x: int(x), line.split(" ")))
    else:
        line = line.strip()
    count += 1
fin.close()
holder = []
for i in range(len(observations)):
    holder.append(i+1)
r_loc = {}
for i in range(len(observations)):
    ai = movement[i]
    r_loc[i+1] = ai
answers = findsort(r_loc, findsort(r_loc, findsort(r_loc, holder)))
fout = open("shuffle.out", "w")
count = len(observations)
for answer in answers:
    if count != 0:
        fout.write("{}\n".format(observations[answer-1]))
    else:
        fout.write("{}".format(observations[answer-1]))
    count += 1
fout.close()
