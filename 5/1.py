from __future__ import print_function

def read(filename):
    return open(filename, 'r').read().strip()

def react(s):
    buf = []
    for c in s:
        if buf and c == buf[-1].swapcase():
            buf.pop()
        else:
            buf.append(c)
    return len(buf)

print(react(read('test.in')))
print(react(read('puzzle.in')))

def best_remove(s):
    return min(react([cc for cc in s if cc.lower() != c]) for c in set(c.lower() for c in s))

print(best_remove(read('test.in')))
print(best_remove(read('puzzle.in')))
