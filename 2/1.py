from collections import defaultdict

def count(s):
    h = defaultdict(int)
    for c in s:
        h[c] += 1
    return (2 in h.values()), (3 in h.values())

assert count("abcdef") == (False, False)
assert count("bababc") == (True, True)
assert count("abbcde") == (True, False)
assert count("abcccd") == (False, True)
assert count("aabcdd") == (True, False)
assert count("abcdee") == (True, False)
assert count("ababab") == (False, True)

def checksum(l):
    n2, n3 = 0, 0
    for s in l:
        l2, l3 = count(s)
        if l2: n2 += 1
        if l3: n3 += 1
    return n2*n3


test = ["abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab"]

assert checksum(test) == 12

real = [s.strip() for s in open("input", "r")]

print(checksum(real))
assert checksum(real) == 7904
