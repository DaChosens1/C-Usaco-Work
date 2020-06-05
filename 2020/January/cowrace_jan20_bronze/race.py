 #time = 34 min
def fin_open():
    fin = open('race.in')
    distance = 0
    x_times = []
    count = 1
    for line in fin:
        line = line.strip()
        if count == 1:
            k, n = line.split(" ")
            distance = int(k)
        else:
            x_times.append(int(line))
        count += 1
    fin.close()
    return distance, x_times


def calc_time(k, x):
    t = 0
    cspeed = 0
    cdist = 0
    while True:
        if cspeed < x:
            cspeed += 1
        else:
            if cspeed == x:
                xdist = cdist
                if cdist + cspeed + 1 >= k:
                    cspeed -= 1
                else:
                    cspeed += 1
            else:
                if (k-xdist)/2 > cdist-xdist:
                    cspeed += 1
                else:
                    cspeed -= 1
        cdist += cspeed
        t += 1
        if cdist >= k:
            break
    return t


def calc_all_times(k_times):
    k = k_times[0]
    times = k_times[1]
    min_speeds = []
    for time in times:
        min_speeds.append(calc_time(k, time))
    return min_speeds


def fout_close(answers):
    fout = open("race.out", "w")
    for answer in answers:
        fout.write("{}\n".format(answer))
    fout.close()


fout_close(calc_all_times(fin_open()))
