# 43 min
def fin_open():
    fin = open('teleport.in')
    for line in fin:
        line = line.strip()
        group = map(lambda x: int(x), line.split(" "))
    fin.close()
    return group


def compute_to_teleport(road):
    start, end, tele1, tele2 = road
    try1 = abs(tele1 - start) + abs(tele2 - end)
    try2 = abs(tele2 - start) + abs(tele1 - end)
    return min([try2, try1])


def fout_close(data):
    fout = open("teleport.out", "w")
    try1 = abs(data[1]-data[0])
    try2 = compute_to_teleport(data)
    fout.write("{}".format(min([try2, try1])))
    fout.close()


fout_close(fin_open())
