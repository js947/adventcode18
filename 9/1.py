from collections import deque

def part1(players, marbles, verbose=False):
    scores = [0]*players
    circle = deque([0])

    for i in range(1, marbles+1):
        if i%23 == 0:
            circle.rotate(7)
            scores[i%len(scores)] += i + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)

    return max(scores)

def part1_expect(players, marbles, expected_score, **kwargs):
    score = part1(players, marbles, **kwargs)
    print(f"part1 with {'%3d'%players} players and {'%6d'%marbles} marbles got {'%7d'%score} expected {'%7d'%expected_score}, {score == expected_score}")
    try:
        assert expected_score == score
    except AssertionError:
        pass

part1_expect(9, 25, 32, verbose=True)
part1_expect(10, 1618, 8317)
part1_expect(13, 7999, 146373)
part1_expect(17, 1104, 2764)
part1_expect(21, 6111, 54718)
part1_expect(30, 5807, 37305)
print(part1(411, 71058))
print(part1(411, 100*71058))
