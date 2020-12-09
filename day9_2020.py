from collections import deque, defaultdict

# clockwise +1, counter -1


def play(players, last_marble):

    scores = defaultdict(int)

    # players = deque(range(1,players+1))

    x = 0
    circle = deque([x])

    while x < last_marble:
        x += 1
        if x % 23 == 0:
            circle.rotate(7)
            scores[x % players] += x + circle.pop()
            circle.rotate(-1)
        else:
            # add marble between 1 and 2 clockwise
            circle.rotate(-1)
            circle.append(x)
        # start = circle.index(0)  # slow!
        # print(list(circle)[start:])
    return max(scores.values())


print("#1", play(419, 71052))
print("#2", play(419, 71052 * 100))


assert play(9, 25) == 32
assert play(10, 1618) == 8317
assert play(13, 7999) == 146373
