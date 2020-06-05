# time = 43 min
def open_file():
    fin = open('herding.in')
    for line in fin:
        line = line.strip()
        cows = list(map(lambda x: int(x), line.split(" ")))
    fin.close()
    return cows


def find_min(data_set):
    if data_set[0]+2 == data_set[1]+1 == data_set[2]:
        return 0
    else:
        if data_set[0] + 2 == data_set[1] or data_set[0] + 2 == data_set[2] or \
           data_set[1] + 2 == data_set[0] or data_set[1] + 2 == data_set[2] or \
           data_set[2] + 2 == data_set[0] or data_set[2] + 2 == data_set[1]:
            return 1
        else:
            return 2


def find_max(data_set):
    if data_set[2]-data_set[1]>data_set[1]-data_set[0]:
        return data_set[2]-data_set[1]-1
    else:
        return data_set[1] - data_set[0] - 1


def compute_min_max(cows):
    minimum = find_min(cows)
    maximum = find_max(cows)
    return [minimum, maximum]


def close_file(answer):
    fout = open("herding.out", "w")
    fout.write("{}\n".format(answer[0]))
    fout.write("{}\n".format(answer[1]))
    fout.close()


close_file(compute_min_max(open_file()))
