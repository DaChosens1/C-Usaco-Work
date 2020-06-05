# time = 43 min
def open_file():
    fin = open('traffic.in')
    count = 1
    ramp = []
    for line in fin:
        if count > 1:
            line = line.strip()
            ramp_type, first, last = line.split()
            ramp.append([ramp_type, int(first), int(last)])
        else:
            line = line.strip()
            n = int(line)
        count += 1
    fin.close()
    return n, ramp


def compute_all(traffic):
    n = traffic[0]
    ramp = traffic[1]
    a = -999999999
    b = 999999999
    range_int = range(-n, 0)
    range_int.reverse()
    for i in range_int:
        if ramp[i][0] == "none":
            a = max(a, ramp[i][1])
            b = min(b, ramp[i][2])
        if ramp[i][0] == "off":
            a += ramp[i][1]
            b += ramp[i][2]
        if ramp[i][0] == "on":
            a -= ramp[i][2]
            b -= ramp[i][1]
            a = max(0, a)
    before = [a, b]
    a = -999999999
    b = 999999999
    for i in range(n):
        if ramp[i][0] == "none":
            a = max(a, ramp[i][1])
            b = min(b, ramp[i][2])
        if ramp[i][0] == "on":
            a += ramp[i][1]
            b += ramp[i][2]
        if ramp[i][0] == "off":
            a -= ramp[i][2]
            b -= ramp[i][1]
            a = max(0, a)
    after = [a, b]
    return before, after


def close_file(answer):
    fout = open("traffic.out", "w")
    fout.write("{} {}\n".format(answer[0][0], answer[0][1]))
    fout.write("{} {}\n".format(answer[1][0], answer[1][1]))
    fout.close()


close_file(compute_all(open_file()))
