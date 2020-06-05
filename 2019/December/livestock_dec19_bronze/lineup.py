import copy


def fin_open():
    fin = open('lineup.in')
    count = 1
    pairs = []
    for line in fin:
        line = line.strip()
        if count == 1:
            pass
        else:
            x = line.split(" must be milked beside ")
            x.sort()
            pairs.append(x)
        count += 1
    fin.close()
    return pairs


def find_ans(constraints):
    a = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
    for fir in a:
        b = copy.copy(a)
        b.remove(fir)
        for sec in b:
            c = copy.copy(b)
            c.remove(sec)
            for third in c:
                d = copy.copy(c)
                d.remove(third)
                for four in d:
                    e = copy.copy(d)
                    e.remove(four)
                    for fif in e:
                        f = copy.copy(e)
                        f.remove(fif)
                        for six in f:
                            g = copy.copy(f)
                            g.remove(six)
                            for sev in g:
                                h = copy.copy(g)
                                h.remove(sev)
                                for eight in h:
                                    temp = [fir, sec, third, four, fif, six, sev, eight]
                                    works = True
                                    for n in constraints:
                                        if temp.index(n[0]) == temp.index(n[1])+1 or temp.index(n[0]) == temp.index(n[1])-1:
                                            pass
                                        else:
                                            works = False
                                            break
                                    if works:
                                        return temp


def fout_close(answer):
    fout = open("lineup.out", "w")
    for ans in answer:
        fout.write("{}\n".format(ans))
    fout.close()


fout_close(find_ans(fin_open()))
