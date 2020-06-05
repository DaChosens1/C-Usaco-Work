# time = 36 min
def open_file():
    fin = open('cownomics.in')
    spotted_cows = []
    plain_cows = []
    count = -1
    cows = 0
    for line in fin:
        line = line.strip()
        if cows == 0:
            n, m = map(lambda x: int(x), line.split(" "))
            cows = n
        elif count < cows:
            spotted_cows.append(line[::])
        else:
            plain_cows.append(line[::])
        count += 1
    fin.close()
    return spotted_cows, plain_cows


def follow_through(cows):
    pos_spots = 0
    spotted_cows, plain_cows = cows
    for dna_line in range(len(spotted_cows[0])):
        dna_works = True
        for cow in spotted_cows:
            for other_cow in plain_cows:
                if cow[dna_line] == other_cow[dna_line]:
                    dna_works = False
        if dna_works:
            pos_spots += 1
    return pos_spots


def close_file(answer):
    fout = open("cownomics.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(follow_through(open_file()))
