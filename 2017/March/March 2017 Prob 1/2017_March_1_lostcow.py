# time = 43 min
def open_file():
    fin = open('lostcow.in')
    for line in fin:
        line = line.strip()
        places = map(lambda x: int(x), line.split(" "))
    fin.close()
    return places


def follow_through(places):
    person = places[0]
    cow = places[1]
    change_factor = 1
    dist = 0
    while True:
        moved = 0
        for move in range(abs(places[0]-person)+abs(change_factor)):
            if change_factor >= 0:
                person += 1
            else:
                person -= 1
            moved += 1
            dist += 1
            if person == cow:
                return dist
        change_factor *= -2


def close_file(answer):
    fout = open("lostcow.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
