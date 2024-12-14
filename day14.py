import sys
import re
w = 101
h = 103
t = 100
q1,q2,q3,q4 = 0,0,0,0
for line in sys.stdin:
    m = re.match(r"p=(\d+),(\d+) v=([\-]?\d+),([\-]?\d+)", line)
    x = int(m.group(1))
    y = int(m.group(2))
    vx = int(m.group(3))
    vy = int(m.group(4))
    sim_x = (x + t*vx) % w
    sim_y = (y + t*vy) % h
    if sim_x == w // 2 or sim_y == h // 2:
        continue
    if sim_x < w // 2 and sim_y < h // 2:
        q1 += 1
    if sim_x > w // 2 and sim_y < h // 2:
        q2 += 1
    if sim_x > w // 2 and sim_y > h // 2:
        q3 += 1
    if sim_x < w // 2 and sim_y > h // 2:
        q4 += 1
print(q1*q2*q3*q4)
