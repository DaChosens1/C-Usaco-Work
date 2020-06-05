# time = 45 min
def open_file():
    fin = open('cowqueue.in')
    cows = []
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            cows.append(map(lambda x: int(x), line.split(" ")))
        count += 1
    fin.close()
    cows.sort()
    return cows


def follow_through(cows):
    time = 0
    for cow in cows:
        if cow[0] > time:
            time = cow[0]
            time += cow[1]
        else:
            time += cow[1]
    return time


def close_file(answer):
    fout = open("cowqueue.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
