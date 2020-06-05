def area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)


def leftover_area(input_list, changer_list):
    [x1, y1], [x2, y2] = input_list
    [x3, y3], [x4, y4] = changer_list
    visible_area = area(x1, y1, x2, y2)
    leftmostblockedx = max(x1, x3)
    rightmostblockedx = min(x2, x4)
    bottommostblockedy = max(y1, y3)
    topmostblockedy = min(y2, y4)
    if leftmostblockedx < rightmostblockedx and bottommostblockedy < topmostblockedy:
        visible_area -= area(leftmostblockedx, bottommostblockedy, rightmostblockedx, topmostblockedy)
    return visible_area


fin = open('billboard.in')
# fin = open('ex.txt')
billboard1 = []
billboard2 = []
truck = []
count = 1
for line in fin:
    if count == 1:
        line = line.strip()
        x1, y1, x2, y2 = list(map(lambda x: int(x), line.split(' ')))
        billboard1 = [[x1, y1], [x2, y2]]
    if count == 2:
        line = line.strip()
        x1, y1, x2, y2 = list(map(lambda x: int(x), line.split(' ')))
        billboard2 = [[x1, y1], [x2, y2]]
    if count == 3:
        line = line.strip()
        x1, y1, x2, y2 = list(map(lambda x: int(x), line.split(' ')))
        truck = [[x1, y1], [x2, y2]]
    count += 1
fin.close()
board1 = leftover_area(billboard1, truck)
board2 = leftover_area(billboard2, truck)
fout = open("billboard.out", "w")
fout.write("{}".format(board1 + board2))
fout.close()
