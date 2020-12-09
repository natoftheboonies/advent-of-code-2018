# https://adventofcode.com/2018/day/8
# rewrite 8-Dec-2020

def part1(tree):

    def readtree(cursor):
        metadata = list()
        a,b = tree[cursor:cursor+2]
        cursor += 2
        # read child nodes
        for x in range(a):
            cursor, submeta = readtree(cursor)
            metadata.extend(submeta)
        metadata.extend(tree[cursor:cursor+b])
        cursor += b
        return cursor, metadata

    cursor, metadata = readtree(0)

    return sum(metadata)


def part2(tree):

    def readtree(cursor):
        value = 0
        a,b = tree[cursor:cursor+2]
        cursor += 2
        # read child nodes
        child_values = dict()
        for x in range(a):
            cursor, child_value = readtree(cursor)
            child_values[x] = child_value
        value += sum((child_values.get(x-1,0) for x in tree[cursor:cursor+b]))
        if a == 0:
            value += sum(tree[cursor:cursor+b])
        cursor += b
        return cursor, value

    cursor, value = readtree(0)

    return value

sample = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
sample_tree = list(map(int,sample.split()))

assert part1(sample_tree)==138
assert part2(sample_tree)==66

with open('input8.txt') as fp:
    input_tree = list(map(int,fp.read().strip().split()))

print('#1',part1(input_tree))
print('#2',part2(input_tree))


