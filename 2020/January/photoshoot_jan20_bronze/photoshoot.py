 #time = 53 min
def open_file():
    fin = open('photo_bronze_jan20/1.in')
    count = 1
    for line in fin:
        line = line.strip()
        if count == 1:
            pass
        else:
            line = map(lambda x: int(x), line.split(" "))
        count += 1
    fin.close()
    return line


def nums_repeat(list_check):
    var = False
    for n in range(len(list_check)):
        for i in range(len(list_check)):
            if n!=i and list_check[n]==list_check[i]:
                var=True
                break
        if var:
            break
    return var

def follow_through(line):
    og_line = []
    count = 1
    while True:
        og_line.append(count)
        for num in range(len(line)):
            if nums_repeat(og_line):
                og_line = []
                break
            else:
                if line[num] - og_line[num] <= 0:
                    og_line = []
                    break
                else:
                    og_line.append(line[num] - og_line[num])
        if og_line:
            break
        count += 1
    return og_line


def close_file(answer):
    answer = map(lambda x: str(x), answer)
    c_answer = ""
    for a in answer:
        c_answer = c_answer + a
        if a != answer[len(answer)-1]:
            c_answer = c_answer + " "
    fout = open("photo.txt", "w")
    fout.write(c_answer)
    fout.close()


close_file(follow_through(open_file()))
