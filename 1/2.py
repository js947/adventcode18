from __future__ import print_function

def run(l):
    seen = set()
    seen.add(0)
    current = 0
    while True:
        for i in l:
            current += i
            if current in seen:
                return current
            seen.add(current)
        print("cycle", current, len(seen))

t1 = [+1, -1]
t2 = [+3, +3, +4, -2, -4]
t3 = [-6, +3, +8, +5, -6]
t4 = [+7, +7, -2, -7, -4]

real = [int(i) for i in open('input', 'r')]

print("t1", run(t1), 0)
print("t2", run(t2), 10)
print("t3", run(t3), 5)
print("t4", run(t4), 14)
print("real", run(real))
