# time = 43 min
def open_file():
    fin = open('revegetate_bronze_feb19/4.in')
    preferences = []
    pastures = 0
    count = 1
    for line in fin:
        line = line.strip()
        if count == 1:
            n, m = line.split(" ")
            pastures = int(n)
        else:
            line = map(lambda x: int(x), line.split(" "))
            preferences.append(line)
        count += 1
    fin.close()
    return pastures, preferences


def find_possible_set(pastures, poset, temp_set):
    if pastures == 0:
        poset.append(temp_set)
    else:
        for i in range(1, 5):
            temp = temp_set[:]
            temp.append(i)
            find_possible_set(pastures-1, poset, temp)
        return poset


def follow_through(data_set):
    pastures = data_set[0]
    preferences = data_set[1]
    possible_set = find_possible_set(pastures, [], [])
    final_poset = possible_set[:]
    iter_temp = range(len(possible_set))
    iter_temp.reverse()
    for n in iter_temp:
        for i in preferences:
            if possible_set[n][i[0]-1] == possible_set[n][i[1]-1]:
                try:
                    final_poset.pop(n)
                except:
                    pass
                break
    print(final_poset)
    return final_poset[0]


def close_file(answer):
    ans = ""
    for a in answer:
        ans = ans + str(a)
    fout = open("revegetate.out", "w")
    fout.write(ans)
    fout.close()


close_file(follow_through(open_file()))
