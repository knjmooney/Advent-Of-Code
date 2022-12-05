from requests_cache import CachedSession

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = CachedSession().get('https://adventofcode.com/2015/day/1/input', cookies=cookies).content

print(data.count(ord('(')) - data.count(ord(')')))

p = 0
for i, d in enumerate(data):
    p += 1 if d == ord('(') else -1
    if p == -1:
        print(i + 1)
        break