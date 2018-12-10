from collections import defaultdict
import re

def find_min(f):
    i, sz = 0, [0] * 3
    while not (sz[-1] > sz[-2] < sz[-3]):
        i += 1
        sz.append(f(i))
    return i

def solve(filename):
    xs, ys, dxs, dys = zip(*([int(z) for z in re.findall(r'-?\d+', line)] for line in open(filename, 'r')))

    def evolve(i):
        adv = lambda x, dx: x + i*dx
        nxs = list(map(adv, xs, dxs))
        nys = list(map(adv, ys, dys))
        return nxs, nys

    def vol(i):
        xs, ys = evolve(i)
        return (max(xs) - min(xs))*(max(ys) - min(ys))

    def draw(i):
        xs, ys = evolve(i)
        grid = defaultdict(lambda: ' ')
        for x, y in zip(xs, ys):
            grid[(x, y)] = '#'

        return '\n'.join( ''.join( grid[(x,y)]
            for x in range(min(xs), max(xs)+1))
            for y in range(min(ys), max(ys)+1))

    i = find_min(vol)

    print(i-1)
    print(draw(i-1))

solve('test.in')
solve('puzzle.in')
