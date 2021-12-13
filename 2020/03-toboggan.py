def enumerate2(xs, start=0, step=1):
    for x in xs:
        yield (start, x)
        start += step

data = list(open("./03-input.txt").read().splitlines())

for s in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    data2 = [(d, i, i % len(d), d[i%len(d)]) for i, d in enumerate2(data[::s[1]], step=s[0])]
    print(sum([d[3] == '#' for d in data2]))