 #time = 48 min
def open_file():
    fin = open('word.in')
    count = 1
    k=0
    for line in fin:
        line = line.strip()
        if count == 1:
            n, k = line.split(" ")
        else:
            line = line.split(" ")
        count += 1
    fin.close()
    return k, line


def len_str(lin):
    num = 0
    for n in list(lin):
        if n != " ":
            num += 1
    return num


def follow_through(args):
    line = args[1]
    k = args[0]
    new_line = []
    temp_sub_line = ""
    for l in line:
        if len_str(temp_sub_line+l) <= int(k):
            if temp_sub_line:
                temp_sub_line = temp_sub_line+" "+l
            else:
                temp_sub_line = temp_sub_line + l
        else:
            new_line.append(temp_sub_line)
            temp_sub_line = ""
            temp_sub_line = temp_sub_line+l
    if temp_sub_line:
        new_line.append(temp_sub_line)
    return new_line


def close_file(answer):
    fout = open("word.out", "w")
    for str_ans in answer:
        fout.write("{}\n".format(str_ans))
    fout.close()


close_file(follow_through(open_file()))
