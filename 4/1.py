from datetime import datetime
from collections import namedtuple, defaultdict

Log = namedtuple('Log', ['id', 'sleeps'])

def read_log(filename):
    def gen1():
        i = None
        for line in sorted(open(filename, 'r')):
            d, t, *r = line.split()
            t = datetime.strptime(d+' '+t, '[%Y-%m-%d %H:%M]').minute

            if r[0] == 'Guard':
                if i: yield i
                i = Log(int(r[1][1:]), [])
            if r[0] == 'falls':
                b = t
            if r[0] == 'wakes':
                e = t
                i.sleeps.append((b, e))
    return gen1

def part1(filename):
    log = read_log(filename)
    
    d = defaultdict(int)
    for l in log():
        d[l.id] += sum(e - b for b, e in l.sleeps)
    most_sleepy_id = sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]

    d = defaultdict(int)
    for l in log():
        if l.id != most_sleepy_id: continue
        for b, e in l.sleeps:
            for m in range(b, e):
                d[m] += 1
    most_sleepy_min = sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]

    print('part1 %s id %s min %s checksum %s' %
            (filename, most_sleepy_id, most_sleepy_min, most_sleepy_id*most_sleepy_min))

part1('test.in')
part1('puzzle.in')
print()

def part2(filename):
    log = read_log(filename)

    d = defaultdict(lambda: defaultdict(int))
    for l in log():
        for b, e in l.sleeps:
            for m in range(b, e):
                d[l.id][m] += 1

    d = {g:sorted(s.items(), key=lambda x: x[1], reverse=True)[0] for g, s in d.items()}

    most_sleepy_id, (most_sleepy_min, _) = sorted(d.items(), key=lambda x: x[1][1], reverse=True)[0]

    print('part2 %s id %s min %s checksum %s' %
            (filename, most_sleepy_id, most_sleepy_min, most_sleepy_id*most_sleepy_min))

part2('test.in')
part2('puzzle.in')
