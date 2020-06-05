def open_file():
    fin = open('triangles.in')
    fence_posts = []
    count = 1
    for line in fin:
        line = line.strip()
        if count == 1:
            pass
        else:
            line = map(lambda x: int(x), line.split(" "))
            fence_posts.append(line)
        count += 1
    fin.close()
    return fence_posts


def find_all_combinations(fence_posts):
    combinations = []
    for a in fence_posts:
        for b in fence_posts:
            for c in fence_posts:
                if (a == b or b == c or c == a):
                    pass
                elif (a[0] == b[0] or b[0] == c[0] or a[0] == c[0]) and (a[1] == b[1] or b[1] == c[1] or a[1] == c[1]):
                    combinations.append([a, b, c])

    return combinations


def compute_combinations(combinations):
    max_area = 0
    for i in combinations:
        area = abs(i[0][0]*(i[1][1]-i[2][1]) + i[1][0]*(i[2][1]-i[0][1]) + i[2][0]*(i[0][1]-i[1][1]))
        if area == 61076435:
            print(i)
        if area > max_area:
            max_area = area
    return max_area


def close_file(answer):
    fout = open("triangles.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(compute_combinations(find_all_combinations(open_file())))
