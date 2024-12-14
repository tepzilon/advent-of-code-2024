import re


class Space:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.robots = []

    def add_robot(self, r):
        self.robots.append(r)

    def get_area(self, t):
        area = [] * self.h
        for i in range(self.h):
            area.append([0] * self.w)
        for r in self.robots:
            x, y = r.simulate(t, self.w, self.h)
            area[y][x] += 1
        return area

    def safety_factor(self, t):
        q1,q2,q3,q4 = 0,0,0,0
        for r in self.robots:
            x, y = r.simulate(t, self.w, self.h)
            if x == self.w // 2 or y == self.h // 2:
                continue
            if x < self.w // 2 and y < self.h // 2:
                q1 += 1
            if x > self.w // 2 and y < self.h // 2:
                q2 += 1
            if x > self.w // 2 and y > self.h // 2:
                q3 += 1
            if x < self.w // 2 and y > self.h // 2:
                q4 += 1
        print(q1*q2*q3*q4)


class Robot:
    def __init__(self, x: int, y: int, vx: int, vy: int):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def simulate(self, t, w, h):
        return ((self.x + t * self.vx) % w), ((self.y + t * self.vy) % h)

    def __str__(self):
        return f"Robot({self.x=},{self.y=},{self.vx=},{self.vy=})"


space = Space(101, 103)

with open("day14-in.txt", "r") as file:
    for line in file:
        m = re.match(r"p=(\d+),(\d+) v=([\-]?\d+),([\-]?\d+)", line)
        x = int(m.group(1))
        y = int(m.group(2))
        vx = int(m.group(3))
        vy = int(m.group(4))
        r = Robot(x, y, vx, vy)
        space.add_robot(r)

# observed some weird pattern starting from t=42 and every 103 seconds
t = 42
while True:
    area = space.get_area(t)
    for i in range(space.h):
        for j in range(space.w):
            print(' ' if area[i][j] == 0 else area[i][j], end='')
        print()
    print(f"{t=}")
    input()
    t += 103