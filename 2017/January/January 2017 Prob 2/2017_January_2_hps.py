 #time = 48 min
def open_file():
    fin = open('hps.in')
    rounds = []
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            rounds.append(map(lambda x: int(x), line.split(" ")))
        count += 1
    fin.close()
    return rounds


def follow_through(rounds):
    max_wins = 0
    pos_plays = [1, 2, 3]
    for hoof in pos_plays:
        pos_paper = pos_plays[::]
        pos_paper.remove(hoof)
        for paper in pos_paper:
            scissors = pos_paper[::]
            scissors.remove(paper)
            scissors = scissors[0]
            wins = 0
            for game in rounds:
                if game == [hoof, scissors] or game == [scissors, paper] or game == [paper, hoof]:
                    wins += 1
            if wins >= max_wins:
                max_wins = wins
    return max_wins


def close_file(answer):
    fout = open("hps.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(follow_through(open_file()))