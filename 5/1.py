from __future__ import print_function
import string

def read(filename):
    return open(filename, 'r').read().strip()

def react1(s):
    buf = []
    for c in s:
        if buf and c == buf[-1].swapcase():
            buf.pop()
        else:
            buf.append(c)
    return len(buf)

def react2(s):
    lower = sorted(set(c.lower() for c in s))
    upper = sorted(set(c.upper() for c in s))
    pairs = [a+b for a, b in zip(lower, upper) + zip(upper, lower)]

    while any(p in s for p in pairs):
        for p in pairs:
            s = s.replace(p, "")
    return len(s)

for react in (react1, react2):
    print(react(read('test.in')))
    print(react(read('puzzle.in')))

    def best_remove(s):
        return min(react(s.replace(c,"").replace(c.upper(),"")) for c in set(c.lower() for c in s))
        return min(react([cc for cc in s if cc.lower() != c]) for c in set(c.lower() for c in s))

    print(best_remove(read('test.in')))
    print(best_remove(read('puzzle.in')))

    print()
