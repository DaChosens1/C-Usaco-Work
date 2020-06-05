# 43 min
def fin_open():
    fin = open('hoofball.in')
    count = 1
    for line in fin:
        line = line.strip()
        if count > 1:
            cow = map(lambda x: int(x), line.split(" "))
            cow.sort()
        count += 1
    fin.close()
    return cow


cows = fin_open()


def target(passing_cow):
    location = cows.index(passing_cow)
    if location == 0:
        return cows[location + 1]
    elif cows[location] == cows[-1]:
        return cows[-2]
    else:
        right_dist = abs(cows[location + 1] - cows[location])
        left_dist = abs(cows[location] - cows[location - 1])
        if left_dist <= right_dist:
            return cows[location - 1]
        else:
            return cows[location + 1]


def main_code():
    passto = [0 for n in range(1, len(cows) + 1)]
    balls_needed = 0
    for i in range(len(cows)):
        passto[cows.index(target(cows[i]))] += 1
    for i in range(len(cows)):
        if passto[i] == 0:
            balls_needed += 1
        if target(cows[i]) > cows[i] == target(target(cows[i])) and passto[i] == 1 and passto[cows.index(target(cows[i]))] == 1:
            balls_needed += 1
    return balls_needed


def fout_close(data):
    fout = open("hoofball.out", "w")
    fout.write("{}".format(int(data)))
    fout.close()


fout_close(main_code())
