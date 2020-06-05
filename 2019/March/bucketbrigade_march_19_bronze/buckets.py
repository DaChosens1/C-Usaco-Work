# time = 32 min
def open_file():
    fin = open('buckets.in')
    stage = []
    for line in fin:
        line = line.strip()
        stage.append(line[::])
    fin.close()
    return stage


def find_answer(stage):
    for n in range(10):
        for i in range(10):
            if stage[i][n] == "B":
                barn = [i, n]
            if stage[i][n] == "L":
                lake = [i, n]
            if stage[i][n] == "R":
                rock = [i, n]
    if (barn[0] == lake[0] == rock[0] and (barn[1] > rock[1] > lake[1] or barn[1] < rock[1] < lake[1])) or\
            (barn[1] == lake[1] == rock[1] and (barn[0] > rock[0] > lake[0] or barn[0] < rock[0] < lake[0])):
        x = abs(barn[0] - lake[0]) + abs(barn[1] - lake[1]) + 1
    else:
        x = abs(barn[0]-lake[0]) + abs(barn[1]-lake[1])-1
    return x


def close_file(answer):
    fout = open("buckets.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(find_answer(open_file()))
