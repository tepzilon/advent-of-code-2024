import sys
import re
import math

lines = sys.stdin.readlines()

sum = 0
for i in range(0, len(lines), 4):
    m = re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[i])
    a = int(m.group(1))
    c = int(m.group(2))

    m = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[i+1])
    b = int(m.group(1))
    d = int(m.group(2))

    m = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[i+2])
    p = int(m.group(1)) + 10000000000000
    q = int(m.group(2)) + 10000000000000

    # find solution for
    # ax + by = p
    # cx + dy = q
    # let A be 2x2 matrix a,b,c,d
    # let x be 2x1 matrix x,y
    # let B be 2x1 matrix p,q
    # solution for x = inv(A)*B

    det = a*d - b*c
    # TODO: check det = 0
    x = (d*p - b*q) / det
    y = (-c*p + a*q) / det

    # TODO: check x, y >= 0
    if math.floor(x) == x and math.floor(y) == y:
        sum += 3*x + y

print(int(sum))
