import time


# time = 45 min
def open_file():
    fin = open('hopscotch_bronze/14.in')
    grid = []
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            grid.append([char for char in line])
        count += 1
    fin.close()
    return grid


def follow_through(grid):
    places = [[0, 0]]
    while True:
        changed = False
        for place in range(len(places)):
            pos_next_point = []
            for row in range(places[place][0]+1, len(grid)):
                for col in range(places[place][1]+1, len(grid[0])):
                    if grid[row][col] != grid[places[place][0]][places[place][1]]:
                        pos_next_point.append([row, col])
                        changed = True
            places[place] = pos_next_point if pos_next_point != [] else [places[place]]
        places = [j for i in places for j in i]
        if not changed:
            break

    answer = 0
    for place in places:
        if place == [len(grid)-1, len(grid[0])-1]:
            answer += 1
    return answer


def close_file(data):
    fout = open("hopscotch.out", "w")
    fout.write("{}".format(data))
    fout.close()


t1 = time.time()
close_file(follow_through(open_file()))
t2 = time.time()
print(t2 - t1)
