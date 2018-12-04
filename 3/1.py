from __future__ import print_function
from collections import namedtuple, defaultdict
import re

Claim = namedtuple('Claim', ['idx', 'x', 'y', 'dx', 'dy'])

def read_claims(filename):
    def gen():
        for line in open(filename, 'r'):
            yield Claim(*map(int, re.findall(r'\d+', line)))
    return gen

def claimed_cells(c):
    for i in range(c.x, c.x+c.dx):
        for j in range(c.y, c.y+c.dy):
            yield i, j

def map_claims(claims):
    h=defaultdict(int)
    for c in claims():
        for loc in claimed_cells(c):
            h[loc] += 1
    return h

def count_overlaps(claims):
    return sum(1 for count in map_claims(claims).values() if count > 1)

assert count_overlaps(read_claims('test.in')) == 4
assert count_overlaps(read_claims('puzzle.in')) == 121259

def find_nonoverlapping(claims):
    h = map_claims(claims)
    return [c for c in claims() if all(h[loc] == 1 for loc in claimed_cells(c))][0]

assert find_nonoverlapping(read_claims('test.in')).idx == 3
assert find_nonoverlapping(read_claims('puzzle.in')).idx == 239
