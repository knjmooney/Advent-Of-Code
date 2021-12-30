def isvalid(i):
    s = list(str(i))
    return (
        sorted(s) == s and
        2 in [s.count(str(i)) for i in range(10)]
    )

lower, upper = (372304, 847060)
print(sum(isvalid(i) for i in range(lower, upper)))
