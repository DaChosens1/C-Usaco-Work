 #time = 48 min
def open_file():
    fin = open('notlast.in')
    logs = []
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            logs.append([line.split(" ")[0], int(line.split(" ")[1])])
        count += 1
    fin.close()
    return logs


def follow_through(logs):
    cows_milk_data = [0, 0, 0, 0, 0, 0, 0]
    for log in logs:
        if "Bessie" == log[0]:
            cows_milk_data[0] += log[1]
        elif "Elsie" == log[0]:
            cows_milk_data[1] += log[1]
        elif "Daisy" == log[0]:
            cows_milk_data[2] += log[1]
        elif "Gertie" == log[0]:
            cows_milk_data[3] += log[1]
        elif "Annabelle" == log[0]:
            cows_milk_data[4] += log[1]
        elif "Maggie" == log[0]:
            cows_milk_data[5] += log[1]
        elif "Henrietta" == log[0]:
            cows_milk_data[6] += log[1]
    min_milk = min(cows_milk_data)
    for n in range(len(cows_milk_data)):
        try:
            cows_milk_data[cows_milk_data.index(min_milk)] = 1000000000
        except:
            break
    if cows_milk_data == [] or cows_milk_data.count(min(cows_milk_data)) > 1:
        return "Tie"
    else:
        if cows_milk_data[0] == min(cows_milk_data):
            return "Bessie"
        if cows_milk_data[1] == min(cows_milk_data):
            return "Elsie"
        if cows_milk_data[2] == min(cows_milk_data):
            return "Daisy"
        if cows_milk_data[3] == min(cows_milk_data):
            return "Gertie"
        if cows_milk_data[4] == min(cows_milk_data):
            return "Annabelle"
        if cows_milk_data[5] == min(cows_milk_data):
            return "Maggie"
        if cows_milk_data[6] == min(cows_milk_data):
            return "Henrietta"


def close_file(answer):
    fout = open("notlast.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(follow_through(open_file()))