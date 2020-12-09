# another attempt in 2020

with open('input1.txt') as fp:
    changes = [int(line.strip()) for line in fp.readlines()]

print("#1",sum(changes))

visited = set()
freq = 0
while True:
    for c in changes:
        freq += c
        if freq in visited:
            print("#2",freq)
            break
        visited.add(freq)
    else:
        continue
    break