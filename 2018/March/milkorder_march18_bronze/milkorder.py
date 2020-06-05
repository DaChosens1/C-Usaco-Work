# 43 min
def fin_open():
    fin = open('milkorder.in')
    locations = []
    count = 1
    for line in fin:
        line = line.strip()
        if count == 1:
            ncows, nordered, npos = line.split(" ")
        if count == 2:
            order = map(lambda x: int(x), line.split(" "))
        if count > 2:
            locations.append(map(lambda x: int(x), line.split(" ")))
        count += 1
    fin.close()
    return int(ncows), order, locations


def compute_ans(cow_info):
    ncows, order, locations = cow_info
    pos = [[] for n in range(ncows)]
    temp = pos[::]
    for trial in range(ncows):
        works = True
        temp[trial].append(1)
        for pos in locations:
            temp[pos[1]-1].append(pos[0])
        placed_cows = []
        temp1 = []
        for cow in order:
            temp.append(cow)
            if [cow] in temp:
                placed_cows.append(temp[::])
        for cow in range(ncows):
            for c in placed_cows:
                if c[-1] in cow:
                    for n in range(len(c[:-1:])):
                        pass
#                        for n in range()

    return


def fout_close(answer):
    fout = open("tttt.out", "w")
    fout.write("{}\n".format(answer[0]))
    fout.write("{}\n".format(answer[1]))
    fout.close()


fout_close(compute_ans(fin_open()))
