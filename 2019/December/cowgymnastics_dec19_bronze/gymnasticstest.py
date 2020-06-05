def fin_open():
    fin = open('gymnastics.in')
    all_races = []
    count = 1
    for line in fin:
        line = line.strip()
        races = line.split(" ")
        print(races)
        if count == 1:
            pass
        else:
            all_races.append(map(lambda x: int(x), races))
            print(all_races)
        count += 1
    fin.close()
    return all_races


def find_pair(list_nums):
    list_pairs = []
    for n in list_nums:
        for i in list_nums:
            if list_nums.index(n) < list_nums.index(i):
                list_pairs.append([n, i])
    return list_pairs


def find_pairs(races):
    first_race_pairs = find_pair(races[0])
    rest_race_pairs = []
    for n in races[1::]:
        rest_race_pairs.append(find_pair(n))
    return first_race_pairs, rest_race_pairs


def calc_consist_pairs(pairs):
    first_pairs = pairs[0]
    new_first_pairs = []
    rest_pairs = pairs[1]
    n = rest_pairs
    for race in n:
        for pair in race:
            if pair in first_pairs:
                new_first_pairs.append(pair)
        first_pairs = new_first_pairs
        new_first_pairs = []
    return first_pairs


def fout_close(answer):
    fout = open("gymnastics.out", "w")
    print(str(len(answer)))
    fout.write(str(len(answer)))
    fout.close()
    fout_1 = open('gymnastics.out')
    for line in fout_1:
        line = line.strip()
        print(line)
    fout_1.close()
print("hi")
a = calc_consist_pairs(find_pairs(fin_open()))
print(a)
fout_close(a)
