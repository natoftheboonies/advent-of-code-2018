# /usr/bin/env python3

from collections import deque


def parse(lines):
    def parse_coords(c):
        xy, c = c.split("=")
        if ".." in c:
            c = list(map(int, c.split("..")))
            c[1] += 1
        else:
            c = [int(c), int(c) + 1]
        return c

    dirt = {(500, 0): "+"}
    for line in lines:
        a, b = line.split(", ")
        if a[0] == "x":
            x, y = a, b
        else:
            x, y = b, a
        x = parse_coords(x)
        y = parse_coords(y)
        for x1 in range(*x):
            for y1 in range(*y):
                dirt[(x1, y1)] = "#"
    return dirt


def print_dirt(dirt):
    x_range = range(min([x for (x, y) in dirt.keys()]) - 1, max([x for (x, y) in dirt.keys()]) + 2)
    y_range = range(min([y for (x, y) in dirt.keys()]), max([y for (x, y) in dirt.keys()]) + 1)

    for y in y_range:
        for x in x_range:
            print(dirt.get((x, y), "."), end="")
        print()


def write_dirt(dirt, filename="day17.out"):
    x_range = range(min([x for (x, y) in dirt.keys()]), max([x for (x, y) in dirt.keys()]) + 2)
    y_range = range(min([y for (x, y) in dirt.keys()]), max([y for (x, y) in dirt.keys()]) + 1)

    lines = []
    for y in y_range:
        line = ""
        for x in x_range:
            line += dirt.get((x, y), ".")
        line += "\n"
        lines.append(line)

    with open(filename, "w") as fp:
        fp.writelines(lines)


def flow(dirt, pos=(500, 0)):
    infinity = max((y for x, y in dirt.keys()))

    visited = set()
    toflow = deque([(pos[0], pos[1] + 1)])
    while toflow:
        x, y = toflow.popleft()
        visited.add((x, y))
        # first, flow down through sand until infinity
        if dirt.get((x, y + 1), ".") in ".|":
            dirt[(x, y)] = "|"
            if y + 1 <= infinity and (x, y + 1) not in visited:
                toflow.append((x, y + 1))
            continue
        # otherwise, flow left and right
        for side in (x + 1, y), (x - 1, y):
            dirt[(x, y)] = "|"
            if dirt.get(side, ".") in ".|" and side not in visited:
                toflow.append(side)
        # settle water if surrounded by clay: #||||# -> #~~~~#
        lx = x - 1
        while dirt.get((lx, y), ".") in "|~":
            lx -= 1
        rx = x + 1
        while dirt.get((rx, y), ".") in "|~":
            rx += 1
        if dirt.get((lx, y), ".") == "#" and dirt.get((rx, y), ".") == "#":
            for fx in range(lx + 1, rx):
                dirt[(fx, y)] = "~"
                if (fx, y) in toflow:
                    toflow.remove((fx, y))
    return dirt


def part1(dirt):

    # ...within the range of y values in your scan (!!!)
    min_y = min((y for x, y in dirt.keys() if (x, y) != (500, 0)))
    last = (0, 0)
    while True:  # not any(dirt[cell] in '~|' for cell in dirt.keys() if cell[1]==infinity):
        dirt = flow(dirt)
        flowing = len([v for v in dirt.values() if v == "|"])
        settled = len([v for v in dirt.values() if v == "~"])
        if last == (flowing, settled):
            break
        last = (flowing, settled)

    # write_dirt(dirt)
    flowing = len([v for k, v in dirt.items() if v == "|" and k[1] >= min_y])
    settled = len([v for v in dirt.values() if v == "~"])
    return flowing, settled


with open("input17.txt") as fp:
    lines = [line.strip() for line in fp.readlines()]
dirt = parse(lines)
flowing, settled = part1(dirt)
print("#1", flowing + settled)
print("#2", settled)


sample = """\
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
""".splitlines()

sample_dirt = parse(sample)
assert sum(part1(sample_dirt)) == 57
assert part1(sample_dirt)[1] == 29
