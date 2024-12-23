import sys
from queue import Queue
from copy import deepcopy


class Numpad:
    keys = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"],
    ]

    def __init__(self):
        self.seq = ""

    def valid_coord(self, i, j):
        return i >= 0 and i < 4 and j >= 0 and j < 3 and (i, j) != (3, 0)

    def find_key_coord(self, key):
        if key is None:
            return None
        for i in range(4):
            for j in range(3):
                if self.keys[i][j] == key:
                    return (i, j)
        return None

    def press(self, i, j):
        if self.valid_coord(i, j):
            self.seq += self.keys[i][j]

    def get_init_coord(self):
        return (3, 2)

    def get_key(self, i, j):
        if self.valid_coord(i, j):
            return self.keys[i][j]

    def get_state(self):
        return []


class KeypadRobot:
    keys = [
        [None, "^", "A"],
        ["<", "v", ">"],
    ]

    def __init__(self, controlled):
        self.seq = ""

        self.controlled = controlled
        self.controlled_coord = controlled.get_init_coord()

    def up(self):
        (i, j) = self.controlled_coord
        ni, nj = i - 1, j
        if self.controlled.valid_coord(ni, nj):
            self.controlled_coord = (ni, nj)
        self.seq += "^"

    def down(self):
        (i, j) = self.controlled_coord
        ni, nj = i + 1, j
        if self.controlled.valid_coord(ni, nj):
            self.controlled_coord = (ni, nj)
        self.seq += "v"

    def left(self):
        (i, j) = self.controlled_coord
        ni, nj = i, j - 1
        if self.controlled.valid_coord(ni, nj):
            self.controlled_coord = (ni, nj)
        self.seq += "<"

    def right(self):
        (i, j) = self.controlled_coord
        ni, nj = i, j + 1
        if self.controlled.valid_coord(ni, nj):
            self.controlled_coord = (ni, nj)
        self.seq += ">"

    def a(self):
        (i, j) = self.controlled_coord
        self.controlled.press(i, j)
        self.seq += "A"

    def valid_coord(self, i, j):
        return i >= 0 and i < 2 and j >= 0 and j < 3 and (i, j) != (0, 0)

    def find_key_coord(self, key):
        if key is None:
            return None
        for i in range(2):
            for j in range(3):
                if self.keys[i][j] == key:
                    return (i, j)
        return None

    def press(self, i, j):
        if self.valid_coord(i, j):
            key = self.keys[i][j]
            if key == "^":
                self.up()
            elif key == ">":
                self.right()
            elif key == "v":
                self.down()
            elif key == "<":
                self.left()
            elif key == "A":
                self.a()

    def get_init_coord(self):
        return (0, 2)

    def get_key(self, i, j):
        if self.valid_coord(i, j):
            return self.keys[i][j]

    def get_state(self):
        lst = [
            self.controlled.get_key(*self.controlled_coord),
            *self.controlled.get_state(),
        ]
        return tuple(lst)

    def set_controlled_coord(self, i, j):
        if self.controlled.valid_coord(i, j):
            self.controlled_coord = (i, j)

    def set_controlled_key(self, key):
        coord = self.controlled.find_key_coord(key)
        if coord is None:
            return
        self.set_controlled_coord(*coord)


def build_console(a, b, c):
    numpad = Numpad()
    robot1 = KeypadRobot(numpad)
    if c is not None:
        robot1.set_controlled_key(c)
    robot2 = KeypadRobot(robot1)
    if b is not None:
        robot2.set_controlled_key(b)
    console = KeypadRobot(robot2)
    if a is not None:
        console.set_controlled_key(a)
    return console


# pre compute shortest path from state (A, A, n) to (A, A, m)
# where the state tuple is (keypad2_current_key, keypad1_current_key, numpad_current_key)
# using BFS and OOP for managing robots state

shortest = {}
numpad_keys_flatten = [el for row in Numpad.keys for el in row]
for n in numpad_keys_flatten:
    for m in numpad_keys_flatten:
        if n is None or m is None:
            continue
        console = build_console("A", "A", n)
        q = Queue()
        state = console.get_state()
        visited = set([state])
        q.put(console)
        while not q.empty():
            console = q.get()
            console_state = console.get_state()
            if console_state == ("A", "A", m):
                shortest[(n, m)] = console.seq
                break
            # ^
            new_console = deepcopy(console)
            new_console.up()
            new_console_state = new_console.get_state()
            if new_console_state not in visited:
                visited.add(new_console_state)
                q.put(new_console)
            # >
            new_console = deepcopy(console)
            new_console.right()
            new_console_state = new_console.get_state()
            if new_console_state not in visited:
                visited.add(new_console_state)
                q.put(new_console)
            # v
            new_console = deepcopy(console)
            new_console.down()
            new_console_state = new_console.get_state()
            if new_console_state not in visited:
                visited.add(new_console_state)
                q.put(new_console)
            # <
            new_console = deepcopy(console)
            new_console.left()
            new_console_state = new_console.get_state()
            if new_console_state not in visited:
                visited.add(new_console_state)
                q.put(new_console)
            # A
            new_console = deepcopy(console)
            new_console.a()
            new_console_state = new_console.get_state()
            if new_console_state not in visited:
                visited.add(new_console_state)
                q.put(new_console)


def encode(s):
    cur = "A"
    result = ""
    for c in s:
        result += shortest[(cur, c)] + "A"
        cur = c
    return result


sum = 0
for line in sys.stdin:
    line = line.strip()
    seq = encode(line)
    num = int(line[:-1])
    sum += num * len(seq)
    print(line, seq)
print(sum)
