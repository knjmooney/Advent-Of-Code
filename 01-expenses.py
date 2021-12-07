data = [int(x) for x in open("/Users/knjmooney/Downloads/input.txt").read().split()]
data = [(a+b+c, a*b*c, a, b, c) for i in range(1, len(data)) for j in range(i+1, len(data)) for a, b, c in zip(data, data[i:], data[j:])]
ans = [d for d in data if d[0] == 2020]
print(ans)

