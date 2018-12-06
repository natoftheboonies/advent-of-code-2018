import re

pattern = re.compile(r'#\d+ @ (\d+).(\d+): (\d+)x(\d+)')
with open('./input3.txt') as fp:
    fabric = [[0]*1000 for i in range(1000)]
    line = fp.readline()
    while line:
        parse = pattern.match(line.strip())
        if parse:
            a = int(parse.group(1))
            b = int(parse.group(2))
            x = int(parse.group(3))
            y = int(parse.group(4))
            for i in range(x):
                for j in range(y):
                    fabric[a+i][b+j] += 1
        line = fp.readline()

    result = 0
    rows = len(fabric)
    cols = max(map(len, fabric))
    print ("r x c: ", rows, cols)
    for i in range(rows):
        for j in range(cols):
            if fabric[i][j] > 1:
                result += 1

    print(result)
    # find the good elf
    pattern = re.compile(r"""#(\d+) @ (\d+).(\d+): (\d+)x(\d+)""")
    fp.seek(0)
    line = fp.readline()
    while line:
         parse = pattern.match(line.strip())
         if parse:
            elf = int(parse.group(1)) 
            a = int(parse.group(2))
            b = int(parse.group(3))
            x = int(parse.group(4))
            y = int(parse.group(5))
            goodElf = True
            for i in range(x):
                for j in range(y):
                    if fabric[a+i][b+j] > 1:
                        goodElf = False
            if goodElf:
                 print (elf, 'is a good elf')
         line = fp.readline()
