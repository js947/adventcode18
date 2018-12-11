import numpy as np

def powerlevel(x, y, i):
    rackid = x + 10
    power = rackid * y
    power += i
    power *= rackid
    return (power // 100 % 10) - 5

assert powerlevel(3, 5, 8) == 4
assert powerlevel(122, 79, 57) == -5
assert powerlevel(217, 196, 39) == 0
assert powerlevel(101, 153, 71) == 4

def peakpower(i, sz=3):
    p = np.fromfunction(lambda x, y: powerlevel(x, y, i), (300,300), dtype=int)
    w = np.fromfunction(np.vectorize(lambda x, y: np.sum(p[x:x+sz,y:y+sz])), (300-sz,300-sz), dtype=int)
    max_l = np.unravel_index(np.argmax(w), w.shape)
    max_p = np.max(w)
    return max_l, max_p

assert peakpower(18) == ((33,45), 29)
assert peakpower(42) == ((21,61), 30)

print(peakpower(8199))

def peakpower2(i):
    maxpower = (None, -999)
    for sz in range(1,300):
        ((x,y), p) = peakpower(i, sz)
        if p > maxpower[1]:
            maxpower = ((x,y,sz), p)
        print(sz, maxpower)
    return maxpower

#assert peakpower2(18) == ((90,269,16), 113)
#assert peakpower2(42) == ((232,251,12), 119)

print(peakpower2(8199))
