from __future__ import print_function
from collections import Counter

def read(filename):
    def gen():
        for line in open(filename, 'r'):
            yield [int(i) for i in line.split(',')]
    return list(gen())

test_in = read('test.in')
puzzle_in = read('puzzle.in')

def dist(a, b):
    return sum(abs(ax - bx) for ax, bx in zip(a,b))

def part1(inp, verbose=False):
    buf = 2
    xmin = min(x for x, y in inp)
    xmax = max(x for x, y in inp)
    ymin = min(y for x, y in inp)
    ymax = max(y for x, y in inp)

    def min_dist(x, y):
        min_dist = 99999999
        min_cat = "."
        for i, p in enumerate(inp):
            d = dist((x,y), p)
            if d <= min_dist:
                min_cat = i
                if d == min_dist:
                    min_cat = "."
                    continue
                min_dist = d
        return (x, y), min_cat

    def dists():
        for x in range(xmin-buf, xmax+1+buf):
            for y in range(ymin-buf, ymax+1+buf):
                yield min_dist(x, y)
    dists = {i:cat for i, cat in dists()}

    def edges():
        for x in range(xmin-buf, xmax+1+buf):
            yield dists[x, ymin-buf]
            yield dists[x, ymax+buf]
        for y in range(ymin-buf, ymax+1+buf):
            yield dists[xmin-buf, y]
            yield dists[xmax+buf, y]
    edges = set(edges())

    if verbose:
        for x in range(xmin-buf, xmax+1+buf):
            for y in range(ymin-buf, ymax+1+buf):
                print("%2s" % dists[(x,y)], end=" ")
            print()

    return Counter(a for a in dists.values() if a not in edges).most_common(1)[0][1]


part1_test = part1(test_in, verbose=True)
print("part 1 test   ", part1_test)
assert part1_test == 17
part1_puzzle = part1(puzzle_in)
print("part 1 puzzle ", part1_puzzle)
assert part1_puzzle == 6047

def part2(inp, max_dist):
    buf = 8
    xmin = min(x for x, y in inp) - buf
    xmax = max(x for x, y in inp) + buf
    ymin = min(y for x, y in inp) - buf
    ymax = max(y for x, y in inp) + buf

    def in_region(x, y):
        return 1 if sum(dist(p, (x, y)) for p in inp) < max_dist else 0

    def all_regions(f):
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                yield f(x, y)

    return sum(all_regions(in_region))

part2_test = part2(test_in, 32)
print("part 2 test   ", part2_test)
assert part2_test == 16

part2_puzzle = part2(puzzle_in, 10000)
print("part 2 puzzle ", part2_puzzle)
assert part2_puzzle == 46320
