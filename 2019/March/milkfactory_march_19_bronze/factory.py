# time = 32 min
def open_file():
    fin = open('factory.in')
    belts = []
    count = 1
    for line in fin:
        line = line.strip()
        if count == 1:
            n = int(line)
        else:
            belts.append(map(lambda x: int(x), line.split(" ")))
        count += 1
    fin.close()
    return n, belts


def check_if_leads(goal, in_out_list, n):
    if n == goal:
        return True
    else:
        try:
            for i in in_out_list:
                if i[0] == n:
                    x = i[1]
                    break
            check_if_leads(goal, in_out_list, x)
        except:
            return False


def find_answer(stage):
    n = stage[0]
    belts = stage[1]
    answer = -1
    changes = 0
    works = True
    for i in range(n):
        for target in belts:
            if i+1 != target[0]:
                pass
            else:
                works = False
                break
        if works:
            answer = i+1
            changes += 1
        works = True
        if changes >= 2:
            return -1
    return answer
#        answer = i+1
#        for target in range(n-1):
#            if i == target:
#                pass
#            else:
#                if not check_if_leads(i+1, belts, target+1):
#                    pass
#                else:
#                    answer = -1
#                    works = False
#                    break
#        if works:
#            return answer


def close_file(answer):
    fout = open("factory.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(find_answer(open_file()))
