def covered(x, y, x1, y1, x2, y2):
	return x >= x1 and x <= x2 and y >= y1 and y <= y2


def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_coords=[]
    for line in fin:
        line = line.strip()
        if count == 0:
            line = line.split(" ")
            all_coords.append(list(map(lambda x: int(x), line)))
        else:
            line = line.split(" ")
            all_coords.append(list(map(lambda x: int(x), line)))
        count += 1
    fin.close()
    return all_coords


def find_remaining_rect_area(all_coords):
    x1 = all_coords[0][0]
    y1 = all_coords[0][1]
    x2 = all_coords[0][2]
    y2 = all_coords[0][3]
    x3 = all_coords[1][0]
    y3 = all_coords[1][1]
    x4 = all_coords[1][2]
    y4 = all_coords[1][3]
    corner_cover = 0
    covered_area = 0
    if covered(x1, y1, x3, y3, x4, y4):
        corner_cover += 1
    if covered(x1, y2, x3, y3, x4, y4):
        corner_cover += 1
    if covered(x2, y1, x3, y3, x4, y4):
        corner_cover += 1
    if covered(x2, y2, x3, y3, x4, y4):
        corner_cover += 1
    if corner_cover == 0 or corner_cover == 1:
        covered_area = abs((x2-x1)*(y1-y2))
    elif corner_cover == 2:
        x_left = max(x1, x3)
        x_right = min(x2, x4)
        y_left = max(y1, y3)
        y_right = min(y2, y4)
        covered_area = ((x2 - x1) * (y2 - y1) - (x_right - x_left) * (y_right - y_left))
    return covered_area


def output_file(input_num):
    fout = open("billboard.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(find_remaining_rect_area(input_file("billboard.in")))
