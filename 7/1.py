from __future__ import print_function
from collections import defaultdict
from re import findall

def read(filename):
    def gen():
        for line in open(filename, 'r'):
            yield [x.strip() for x in findall(r' [A-Z] ', line)]
    return gen

test_in = read('test.in')
puzzle_in = read('puzzle.in')

def all_items(inp):
    for a, b in inp():
        yield a
        yield b

def mk_deps(inp):
    deps = defaultdict(list)
    for a, b in inp():
        deps[a].append(b)
    return deps

def next_item(items, deps):
    n = sorted(i for i in items if all(i not in blocked for blocked in deps.values()))
    return n[0] if len(n) > 0 else None


def tsort(items, deps):
    while items:
        a = next_item(items, deps)
        yield a
        deps.pop(a, None)
        items.remove(a)

def part1(inp):
    return ''.join(tsort(set(all_items(inp)), mk_deps(inp)))

assert part1(test_in) == 'CABDFE'
assert part1(puzzle_in) == 'BITRAQVSGUWKXYHMZPOCDLJNFE'

def step_length(time_add, s):
    return time_add + 1 - ord('A') + ord(s)

def ptsort(inp, time_add, num_workers, verbose=False):
    workers = [None] * num_workers
    seconds = 0

    items = set(all_items(inp))
    deps = mk_deps(inp)

    def progress(w):
        if w is None: return None
        i, t = w
        t -= 1
        if t <= 0: 
            deps.pop(i, None)
            return None
        return (i, t)

    def assign_work(w):
        if w: return w
        a = next_item(items, deps)
        if not a: return None
        items.remove(a)
        return (a, step_length(time_add, a))

    for seconds in range(0,20000):
        workers = [progress(w) for w in workers]
        workers = [assign_work(w) for w in workers]
        if verbose: print("%3d"%seconds, '\t'.join(str(w) for w in workers))
        if not items and not deps and all(w is None for w in workers):
            return seconds

print(ptsort(test_in, 0, 2, verbose=True))
assert ptsort(test_in, 0, 2) == 15
print(ptsort(puzzle_in, 60, 5))


