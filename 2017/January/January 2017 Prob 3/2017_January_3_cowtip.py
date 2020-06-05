# time = 38 min
def open_file():
    fin = open('cowtip.in')
    grid = []
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            grid.append(map(lambda x: int(x), [char for char in line]))
        count += 1
    fin.close()
    return grid


def follow_through(grid):
    usages = 0
    for row in map(lambda x: -x, range(1, len(grid)+1)):
        for column in map(lambda x: -x, range(1, len(grid[row]) + 1)):
            if grid[row][column] == 1:
                for r in range(len(grid) + 1 + row):
                    for c in range(len(grid) + 1 + column):
                        if grid[r][c] == 0:
                            grid[r][c] = 1
                        elif grid[r][c] == 1:
                            grid[r][c] = 0
                usages += 1
    return usages


def close_file(answer):
    fout = open("cowtip.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
