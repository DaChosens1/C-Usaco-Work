# 43 min
def fin_open():
    fin = open('tttt.in')
    play_board = []
    for line in fin:
        line = line.strip()
        play_board.append([char for char in line])
    fin.close()
    return play_board


def compute_ans(board):
    one_win = []
    two_win = []
    for row in board:
        if row.count(row[0]) == len(row):
            a = row[::]
            a.sort()
            one_win.append([a[0], a[2]])
        if row[0] == row[1] != row[2] or \
                row[1] == row[2] != row[0] or \
                row[2] == row[0] != row[1]:
            a = row[::]
            a.sort()
            two_win.append([a[0], a[2]])
    for column in range(3):
        temp = [board[0][column], board[1][column], board[2][column]]
        if temp.count(temp[0]) == len(temp):
            a = temp[::]
            a.sort()
            one_win.append([a[0], a[2]])
        if temp[0] == temp[1] != temp[2] or \
                temp[1] == temp[2] != temp[0] or \
                temp[2] == temp[0] != temp[1]:
            a = temp[::]
            a.sort()
            two_win.append([a[0], a[2]])
    diagonals = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    if diagonals[0].count(diagonals[0][0]) == len(diagonals[0]):
        a = diagonals[0][::]
        a.sort()
        one_win.append([a[0], a[2]])
    if diagonals[1].count(diagonals[1][0]) == len(diagonals[0]):
        a = diagonals[1][::]
        a.sort()
        one_win.append([a[0], a[2]])
    if diagonals[0][0] == diagonals[0][1] != diagonals[0][2] or \
            diagonals[0][1] == diagonals[0][2] != diagonals[0][0] or \
            diagonals[0][2] == diagonals[0][0] != diagonals[0][1]:
        a = diagonals[0][::]
        a.sort()
        two_win.append([a[0], a[2]])
    if diagonals[1][0] == diagonals[1][1] != diagonals[1][2] or \
            diagonals[1][1] == diagonals[1][2] != diagonals[1][0] or \
            diagonals[1][2] == diagonals[1][0] != diagonals[1][1]:
        a = diagonals[1][::]
        a.sort()
        two_win.append([a[0], a[2]])
    new_one_win = []
    for win in one_win:
        if win not in new_one_win:
            new_one_win.append(win)
    new_two_win = []
    for win in two_win:
        if win not in new_two_win:
            new_two_win.append(win)
    return len(new_one_win), len(new_two_win)


def fout_close(answer):
    fout = open("tttt.out", "w")
    fout.write("{}\n".format(answer[0]))
    fout.write("{}\n".format(answer[1]))
    fout.close()


fout_close(compute_ans(fin_open()))
