data = [d.split(')') for d in open('2019/06-input.txt').read().splitlines()]
G = {}
for a, b in data:
    G[a] = G.get(a, []) + [b]


def check_depths(n, d):
    results = [d]
    if n in G:
        for c in G[n]:
            results.extend(check_depths(c, d + 1))
    return results

orbits = {}
def get_orbits(n, orbit):
    global orbits
    orbits[n] = orbit
    orbit = orbit + [n]
    if n in G:
        for c in G[n]:
            get_orbits(c, orbit)



print(sum(check_depths('COM', 0)))
get_orbits('COM', [])
a = len(orbits['YOU'])
b = len(orbits['SAN'])
c = len(set(orbits['YOU']) & set(orbits['SAN']))
print(a - c + b - c)
