import re

data = open("./input-2.txt").read().splitlines()
data = [(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)) 
        for d in data 
        if (m := re.search(r'(\d+)-(\d+) (\w): (\w+)', d))]

print(sum([(d[3][d[0]-1] == d[2]) != (d[3][d[1]-1] == d[2]) for d in data]))