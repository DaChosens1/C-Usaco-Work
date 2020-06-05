def open_file():
    fin = open('breedflip.in')
    count = 1
    orders = []
    for line in fin:
        line = line.strip()
        if count == 1:
            pass
        else:
            line = [char for char in line]
            orders.append(line)
        count += 1
    fin.close()
    return orders


def compute_orders(orders):
    ans = []
    cur_order = orders[0]
    new_order = orders[1]
    l = len(cur_order)
    for i in range(l):
        if cur_order[i] != new_order[i]:
            ans.append(i)
    finish = len(ans)
    for i in range(len(ans)-1):
        if ans[i] == ans[i+1]-1:
            finish -= 1
    return finish


def close_file(answer):
    fout = open("breedflip.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(compute_orders(open_file()))
