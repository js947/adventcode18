from collections import namedtuple

Node = namedtuple('Node', ['children', 'metadata'])

def read(filename):
    return [int(x) for x in open(filename, 'r').read().split()]

test_in = read('test.in')
puzzle_in = read('puzzle.in')

def parse(arr):
    nchild, nmeta = arr[:2]
    children, rem = [], arr[2:]
    for i in range(nchild):
        c, rem = parse(rem)
        children.append(c)
    meta, rem = rem[:nmeta], rem[nmeta:]
    return Node(children, meta), rem

def visit(n, f):
    yield f(n)
    for nn in n.children:
        yield from visit(nn, f)

test_n, rem = parse(test_in); assert not rem
puzzle_n, rem = parse(puzzle_in); assert not rem

def part1(nn):
    return sum(sum(m) for m in visit(nn, lambda n: n.metadata))

assert part1(test_n) == 138
assert part1(puzzle_n) == 48443


def value(n):
    if not n.children:
        return sum(n.metadata)
    ns = sum(value(n.children[i-1]) if (i-1 >= 0 and i-1 < len(n.children)) else 0 for i in n.metadata)
    return ns

assert value(test_n) == 66
assert value(puzzle_n) == 30063
