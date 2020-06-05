def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_lifeguards = []
    for line in fin:
        line = line.strip()
        if count > 0:
            start, finish = line.split(" ")
            all_lifeguards.append([int(start), int(finish)])
        count += 1
    fin.close()
    all_lifeguards.sort()
    return all_lifeguards


def find_remaining_rect_area(all_lifeguards):
    max_time = 0
    for i in all_lifeguards:
        temp = all_lifeguards.copy()
        temp.remove(i)
        current_time = temp[-1][-1]-temp[-1][0]
        for lifeguard in range(len(temp)-1):
            if temp[lifeguard][1] > temp[lifeguard+1][0]:
                current_time += temp[lifeguard+1][0]-temp[lifeguard][0]
            else:
                current_time += temp[lifeguard][1]-temp[lifeguard][0]
        if current_time>max_time:
            max_time = current_time
    return max_time


def output_file(input_num):
    fout = open("lifeguards.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(find_remaining_rect_area(input_file("lifeguards.in")))
