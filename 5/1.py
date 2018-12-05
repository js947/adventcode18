from __future__ import print_function

def read(filename):
    return [line.strip() for line in open(filename, 'r')][0]

def shrink(s):
    for i, (a, b) in enumerate(zip(s[1:], s[:-1])):
        if a.lower() == b.lower():
            if (a.islower() and b.isupper()) or (a.isupper() and b.islower()):
                return s[:i] + s[i+2:]
    return s

def react(s, verbose=False):
    if verbose:
        print(len(s), s)
    while True:
        s_new = shrink(s)
        if s == s_new:
            break
        s = s_new
        if verbose:
            print(len(s), s)
    return len(s)

print(react(read('test.in'), verbose=True))
#print(react(read('puzzle.in')))

def remove(s, c):
    return [cc for cc in s if cc.lower() != c]


for c in "abcd":
    print(c, react(remove(read('test.in'), c)))

for c in "abcdefghijklmnopqrstuvxyz":
    print(c, react(remove(read('puzzle.in'), c)))
