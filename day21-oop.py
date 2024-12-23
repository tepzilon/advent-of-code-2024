class Numpad:
    def __init__(self):
        self.seq = ""
        self.keys = [["7", "8", "9"],["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]

    def valid_coord(self, i, j):
        return i >= 0 and i < 4 and j >= 0 and j < 3 and (i, j) != (3, 0)

    def press(self, i, j):
        if self.valid_coord(i, j):
            self.seq += self.keys[i][j]
    
    def get_init_coord(self):
        return (3, 2)

    def get_state(self):
        return []

class KeypadRobot:
    def __init__(self, controlled):
        self.seq = ""
        self.keys = [
            [None, ("^", self.up), ("A", self.a)],
            [("<", self.left), ("v", self.down), (">", self.right)],
        ]
        self.controlled = controlled
        self.coord = controlled.get_init_coord()

    def up(self):
        (i, j) = self.coord
        ni, nj = i - 1, j
        if self.controlled.valid_coord(ni, nj):
            self.coord = (ni, nj)
    def down(self):
        (i, j) = self.coord
        ni, nj = i + 1, j
        if self.controlled.valid_coord(ni, nj):
            self.coord = (ni, nj)
    def left(self):
        (i, j) = self.coord
        ni, nj = i, j - 1
        if self.controlled.valid_coord(ni, nj):
            self.coord = (ni, nj)
    def right(self):
        (i, j) = self.coord
        ni, nj = i, j + 1
        if self.controlled.valid_coord(ni, nj):
            self.coord = (ni, nj)
    def a(self):
        (i, j) = self.coord
        self.controlled.press(i, j)

    def valid_coord(self, i, j):
        return i >= 0 and i < 2 and j >= 0 and j < 3 and (i, j) != (0, 0)

    def press(self, i, j):
        if self.valid_coord(i, j):
            (key, action) = self.keys[i][j]
            self.seq += key
            action()
    
    def get_init_coord(self):
        return 0, 2
    
    def get_state(self):
        lst = [self.coord, *self.controlled.get_state(self)]
        return tuple(lst)

r = KeypadRobot(KeypadRobot(KeypadRobot(Numpad())))
seq = input()
for c in seq:
    if c == "^":
        r.up()
    if c == "v":
        r.down()
    if c == "<":
        r.left()
    if c == ">":
        r.right()
    if c == "A":
        r.a()
print(r.controlled.controlled.controlled.seq)
