from __future__ import print_function
from collections import namedtuple, defaultdict

Claim = namedtuple('Claim', ['idx', 'x', 'y', 'dx', 'dy'])

def read_claims(filename):
    for line in open(filename, 'r'):
        idx, _, xy, dxy = line.split()
        idx = int(idx[1:])
        x, y = [int(z) for z in xy[:-1].split(',')]
        dx, dy = [int(z) for z in dxy.split('x')]
        yield Claim(idx, x, y, dx, dy)

def claimed_cells(c):
    for i in range(c.x, c.x+c.dx):
        for j in range(c.y, c.y+c.dy):
            yield i, j

def map_claims(claims):
    h=defaultdict(int)
    for c in claims:
        for loc in claimed_cells(c):
            h[loc] += 1
    return h

def count_overlaps(claims):
    return sum(1 for count in map_claims(claims).values() if count > 1)

for k, c in enumerate(read_claims('test.in')):
    print(c, list(claimed_cells(c)))

print(count_overlaps(read_claims('test.in')))
print(count_overlaps(read_claims('puzzle.in')))

def find_nonoverlapping(claims):
    claims = list(claims)
    h = map_claims(claims)

    def allmine(c):
        for loc in claimed_cells(c):
            if h[loc] > 1:
                return False
        return True

    for c in claims:
        if allmine(c):
            return c
    print('no uniq claim found')

print(find_nonoverlapping(read_claims('test.in')))
print(find_nonoverlapping(read_claims('puzzle.in')))
