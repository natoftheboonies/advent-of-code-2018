from sets import Set
with open('./input1.txt') as fp:
    found = False
    cnt = 0
    loop = 0
    freq = Set()
    while not found:
        fp.seek(0)
        line = fp.readline()
        while line:
            cnt += int(line.strip())
            if cnt in freq:
                print('#2: found freq: {} on loop: {}'.format(cnt, loop))
                found = True
                break
            freq.add(cnt)
            line = fp.readline()
        if loop == 0:
            print("#1: {}".format(cnt))
        loop+=1
