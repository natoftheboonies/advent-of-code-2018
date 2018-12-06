from collections import Counter
from sets import Set
with open('./input2.txt') as fp:
    x = 0
    y = 0
    s = Set()
    line = fp.readline()
    while line:
        id = line.strip()
        counts = Counter(id)
        for i in id:
            if counts[i] == 2:
                x+=1
                break
        for i in id:
            if counts[i] == 3:
                y+=1
                break
        for box in s:
            diffs = 0
            for i, c in enumerate(id):
                if box[i] != c:
                    diffs += 1
            if diffs == 1:
                print (box)
                print (id)
                net = ''
                for i, c in enumerate(id):
                    if box[i] == c:
                        net+=c
                print ('#2: {}'.format(net))
        s.add(id)
        line = fp.readline()

    print('#1: {} '.format(x*y))
    fp.seek(0)

