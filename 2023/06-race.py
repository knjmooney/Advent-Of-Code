"""
Solved on my phone.
"""

from math import sqrt,ceil

t = 48989083
d = 390110311121360

f =sqrt(t**2 - 4*d)
print(ceil((t + f) / 2) - ceil((t - f) / 2))
