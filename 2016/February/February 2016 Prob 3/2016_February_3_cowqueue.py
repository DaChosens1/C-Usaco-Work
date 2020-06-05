import itertools as it

fin = open('balancing.in', 'r')
fout = open('balancing.out', 'w')
xcows = []
ycows = []
mincows = 10000
N, B = map(int, fin.readline().split())
for i in range(N):
    x1, y1 = map(int, fin.readline().split())
    xcows.append(x1)
    ycows.append(y1)

xlow, ylow, xhigh, yhigh = 0, 0, 0, 0

xmedian = -1
xxcows = sorted(xcows)
yycows = sorted(ycows)
for xx, yy in it.product(xcows, ycows):
    counts = [0, 0, 0, 0]
    for x, y in cows:
        ew = 0 if x < xx else 2
        ns = 0 if y < yy else 1
        counts[ew + ns] += 1

    mini = max(counts)

if len(xxcows) % 2 == 0:
    med = len(xxcows) // 2
    xmedian = int(xxcows[med] + xxcows[med - 1]) // 2
else:
    med = len(xxcows) // 2
    xmedian = xxcows[med]
xlow = (xmedian // 2) - 1
xhigh = (xmedian // 2) + 1

ymedian = -1
if len(yycows) % 2 == 0:
    med = len(yycows) // 2
    ymedian = int(yycows[med] + yycows[med - 1]) // 2
else:
    med = len(yycows) // 2
    ymedian = yycows[med]

ylow = (ymedian // 2) - 1
yhigh = (ymedian // 2) + 1

for xx in range(xlow - 1, xhigh + 2):
    for yy in range(ylow - 1, yhigh + 2):
        # place boundary at x = xx and y = yy and count cows in each quadrant
        q1, q2, q3, q4 = 0, 0, 0, 0
        for q in range(len(xcows)):
            if xcows[q] < xx * 2 and ycows[q] > yy * 2:
                q1 += 1
            elif xcows[q] > xx * 2 and ycows[q] > yy * 2:
                q2 += 1
            elif xcows[q] < xx * 2 and ycows[q] < yy * 2:
                q3 += 1
            elif xcows[q] > xx * 2 and ycows[q] < yy * 2:
                q4 += 1
        mini = max(q1, q2, q3, q4)
        if mincows > mini:
            mincows = mini

fout.write(str(mincows))
fin.close()
fout.close()
