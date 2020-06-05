fin = open('backforth.in')
#fin = open('mixmilk.txt')
barn1 = []
barn2 = []
count=1
for line in fin:
    line = line.strip()
    a = list(map(lambda x: int(x), line.split(' ')))
    if count==1:
        barn1=a
    else:
        barn2=a
    count+=1
fin.close()
all_pos=[]
value_hold=1000
for tues in barn1:
    two=barn2.copy()
    two.append(tues)
    for wed in two:
        three=barn1.copy()
        three.remove(tues)
        three.append(wed)
        for thurs in three:
            four=two.copy()
            four.remove(wed)
            four.append(thurs)
            for fri in four:
                value_hold-=tues
                value_hold+=wed
                value_hold-=thurs
                value_hold+=fri
                if value_hold not in all_pos:
                    all_pos.append(value_hold)
                value_hold=1000
#print(len(all_pos))
fout = open("backforth.out", "w")
fout.write("{}".format(len(all_pos)))
fout.close()
