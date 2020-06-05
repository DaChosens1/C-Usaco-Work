def fin_open():
    fin = open('whereami.in')
    count = 1
    for line in fin:
        line = line.strip()
        if count == 1:
            n = line
        else:
            r = line
        count += 1
    fin.close()
    return int(n), r


def calculate_sections(num, mboxes):
    sections = []
    for n in range(len(mboxes)-num+1):
        sections.append(mboxes[n:n+num:])
    return sections


def calc_equality(usages):
    letters = usages[0]
    mailboxes = usages[1]
    solution = letters
    for n in range(letters):
        sub_section = calculate_sections(n+1, mailboxes)
        if solution != letters:
            break
        for x in range(len(sub_section)):
            d = [inner_list[:] for inner_list in sub_section]
            d.pop(x)
            if sub_section[x] in d:
                solution = letters
                break
            else:
                solution = n+1
    return solution


def fout_close(answer):
    fout = open("whereami.out", "w")
    fout.write("{}".format(answer))
    fout.close()


fout_close(calc_equality(fin_open()))
