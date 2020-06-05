# 56 min
def fin_open():
    fin = open('taming.in')
    count = 1
    cows = []
    for line in fin:
        line = line.strip()
        if count > 1:
            cow = map(lambda x: int(x), line.split(" "))
            for n in cow:
                if n == -1:
                    cows.append([n, -1])
                if n > 0:
                    cows.append([n, False])
                if n == 0:
                    cows.append([n, True])
        count += 1
    fin.close()
    cows[0] = [0, True]
    return cows


def main_code(cows):
    logs = cows[::][::]
    logs.reverse()
    for log in range(len(logs)):
        if (logs[log][1] is True and logs[log][0] > 0) or (logs[log][1] is False and logs[log][0] == 0):
            return -1
        if logs[log][0] > 0:
            logs[log + logs[log][0]][1] = True
            for n in range(log, log + logs[log][0]):
                logs[n][1] = False

    breakouts = 0
    cha_factor = 0
    for ans in logs:
        if ans[1] is True:
            breakouts += 1
        if ans[1] == -1:
            cha_factor += 1
    return "{} {}".format(breakouts, breakouts + cha_factor)


def fout_close(answer):
    fout = open("taming.out", "w")
    fout.write("{}".format(answer))
    fout.close()


fout_close(main_code(fin_open()))
