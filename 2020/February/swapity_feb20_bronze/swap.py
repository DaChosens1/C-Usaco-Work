def open_file():
    fin = open('swap_bronze_feb20/1.in')
    k_swaps = []
    count = 1
    for line in fin:
        line = line.strip()
        if count == 1:
            n, k = line.split(" ")
            nlist = list(range(1, int(n)+1))
        else:
            line = list(map(lambda x: int(x), line.split(" ")))
            k_swaps.append(line)
        count += 1
    fin.close()
    return nlist, int(k), k_swaps


def swap_section(line_swapping, indexes):
    reversed_list = line_swapping[indexes[0]-1:indexes[1]:]
    reversed_list.reverse()
    final_list = []
    done = False
    for i in range(len(line_swapping)):
        if not (indexes[0] <= i + 1 <= indexes[1]):
            final_list.append(line_swapping[i])
        elif not done:
            final_list.extend(reversed_list)
            done = True

    return final_list


def calculate_swaps(data_vals):
    nlist = data_vals[0]
    k_swaps = data_vals[2]
    if k_swaps[0][1]-k_swaps[0][0] < k_swaps[1][1]-k_swaps[1][0]:
        k = data_vals[1] % (k_swaps[0][1]-k_swaps[0][0]+1)
    else:
        k = data_vals[1] % (k_swaps[1][1] - k_swaps[1][0]+1)
    if k_swaps[0][0]<k_swaps[0][1] < k_swaps[1][0]<k_swaps[1][1] or k_swaps[1][0]<k_swaps[1][1]<k_swaps[0][0] < k_swaps[0][1] or k_swaps[1][1]-k_swaps[1][0]+1 == len(nlist) or k_swaps[0][1]-k_swaps[0][0]+1 == len(nlist):
        k = data_vals[1] % 4
    for i in range(k):
        nlist = swap_section(nlist, k_swaps[0])
        nlist = swap_section(nlist, k_swaps[1])
    return nlist


def close_file(answer):
    fout = open("swap.out", "w")
    for ans in answer:
        fout.write("{}\n".format(ans))
    fout.close()


close_file(calculate_swaps(open_file()))
