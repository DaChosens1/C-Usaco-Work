# time = 43 min
def open_file():
    fin = open('circlecross.in')
    for line in fin:
        line = line.strip()
        cows = [char for char in line]
    fin.close()
    return cows


def follow_through(cows):
    intersections = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for letter in letters:
        new_loop = letters[::]
        new_loop.remove(letter)
        for new_letter in new_loop:
            letter_index = []
            new_letter_index = []
            for cow in range(len(cows)):
                if cows[cow] == letter:
                    letter_index.append(cow)
                if cows[cow] == new_letter:
                    new_letter_index.append(cow)
                if len(letter_index) == 2 and len(new_letter_index) == 2:
                    break
            if (letter_index[0] < new_letter_index[0] < letter_index[1] < new_letter_index[1] or new_letter_index[0] <
                    letter_index[0] < new_letter_index[1] < letter_index[1]):
                to_be_added = [letter, new_letter]
                to_be_added.sort()
                if to_be_added not in intersections:
                    intersections.append(to_be_added)
    return len(intersections)


def close_file(answer):
    fout = open("circlecross.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
