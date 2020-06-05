# time = 36 min
def open_file():
    fin = open('art.in')
    grid = []
    count = 0
    for line in fin:
        line = line.strip()
        if count > 0:
            grid.append(map(lambda x: int(x), line[::]))
        count += 1
    fin.close()
    return grid


def follow_through(grid):
    relations = []
    cows = list(set([j for i in [list(set(row)) for row in grid] for j in i]))
    try:
        cows.remove(0)
    except:
        pass
    cow_points = [[] for n in range(len(cows))]
    for cow in cows:
        for row in range(len(grid)):
            for column in range(len(grid)):
                if grid[row][column] == cow:
                    cow_points[cows.index(cow)].append([row, column])
    cow_rect = [[] for n in range(len(cows))]
    for cow in cow_points:
        x_vals = []
        y_vals = []
        for point in cow:
            x_vals.append(point[1])
            y_vals.append(point[0])
        cow_rect[cow_points.index(cow)] = [min(y_vals), max(y_vals), min(x_vals), max(x_vals)]
    for row in range(len(grid)):
        for column in range(len(grid)):
            rect_in = []
            for cow in cow_rect:
                if cow[0] <= row <= cow[1] and cow[2] <= column <= cow[3]:
                    rect_in.append(cows[cow_rect.index(cow)])
            try:
                rect_in.remove(grid[row][column])
            except:
                pass
            for cow in rect_in:
                relations.append([grid[row][column], cow])
    answer = cows[::]
    for relation in relations:
        try:
            answer.remove(relation[0])
        except:
            pass
    return len(answer)


def close_file(answer):
    fout = open("art.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(follow_through(open_file()))
