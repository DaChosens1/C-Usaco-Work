# time = 43 min
def open_file():
    fin = open('crossroad.in')
    cows = [[1, []], [2, []], [3, []], [4, []], [5, []], [6, []], [7, []], [8, []], [9, []], [10, []]]
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            line = map(lambda x: int(x), line.split(" "))
            for n in cows:
                if line[0] == n[0]:
                    n[1].append(line[1])
        count += 1
    fin.close()
    return cows


def follow_through(cows):
    to_be_deleted = []
    for n in range(10):
        if cows[n][1] == []:
            to_be_deleted.append(n)
    to_be_deleted.reverse()
    for n in to_be_deleted:
        cows.pop(n)
    crossings = 0
    for cow in cows:
        original_pos = cow[1][0]
        for places in cow[1]:
            if places != original_pos:
                crossings += 1
                original_pos = places
    return crossings


def close_file(answer):
    fout = open("crossroad.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
