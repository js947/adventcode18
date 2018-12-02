
def compare(a, b):
    return sum(1 for ca, cb in zip(a, b) if ca != cb)

test = [
"abcde",
"fghij",
"klmno",
"pqrst",
"fguij",
"axcye",
"wvxyz"]

def find_similar(l):
    for a in l:
        for b in l:
            if compare(a, b) == 1:
                return ''.join(ca for ca, cb in zip(a, b) if ca == cb)

assert find_similar(test) == 'fgij'

real = [s.strip() for s in open("input", "r")]

print(find_similar(real))
assert find_similar(real) == 'wugbihckpoymcpaxefotvdzns'
