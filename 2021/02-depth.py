import re
data = open("./02-input.txt").read().splitlines()
data = [(m.group(1), int(m.group(2))) for d in data if (m := re.search(r'(\w+) (\d+)', d))]
h = sum([d[1] for d in data if d[0] == "forward"])
d = sum([d[1] for d in data if d[0] == "down"]) - sum([d[1] for d in data if d[0] == "up"])
print((d, h, d*h))

aim = 0
h = 0
d = 0
for dir, v in data:
    if dir == 'forward':
        h += v
        d += v * aim
    if dir == 'up':
        aim -= v
    if dir == 'down':
        aim += v
print(h, d, h*d)
