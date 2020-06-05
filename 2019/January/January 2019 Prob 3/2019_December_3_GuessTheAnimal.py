def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_animals = []
    for line in fin:
        line = line.strip()
        if count > 0:
            line = line.split(" ")
            all_animals.append(line[2::])
        count += 1
    fin.close()
    return all_animals


def find_max_common_pairs(all_animals):
    max_pairs = 0
    for animal in range(len(all_animals)):
        for n in range(len(all_animals)):
            if animal is not n:
                if len(list(set(all_animals[animal]) & set(all_animals[n]))) > max_pairs:
                    max_pairs = len(list(set(all_animals[animal]) & set(all_animals[n])))
    return max_pairs+1


def output_file(input_num):
    fout = open("guess.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(find_max_common_pairs(input_file("guess.in")))
