import sys
from queue import Queue

numpad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

numpad_coord = {}
for i in range(4):
    for j in range(3):
        if numpad[i][j] is None:
            continue
        numpad_coord[numpad[i][j]] = (i, j)

numpad_path = {}
for num, coord in numpad_coord.items():
    q = Queue()
    visited = set([coord])
    q.put((coord, ""))
    while not q.empty():
        ((i, j), path) = q.get()
        numpad_path[(num, numpad[i][j])] = path
        for move, di, dj in [("^", -1, 0), (">", 0, 1), ("v", 1, 0), ("<", 0, -1)]:
            ni, nj = i + di, j + dj
            if (
                ni >= 0
                and ni < 4
                and nj >= 0
                and nj < 3
                and (ni, nj) != (3, 0)
                and (ni, nj) not in visited
            ):
                visited.add((ni, nj))
                q.put(((ni, nj), path + move))

keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]

keypad_coord = {}
for i in range(2):
    for j in range(3):
        if keypad[i][j] is None:
            continue
        keypad_coord[keypad[i][j]] = (i, j)

keypad_path = {}
for key, coord in keypad_coord.items():
    q = Queue()
    visited = set([coord])
    q.put((coord, ""))
    while not q.empty():
        ((i, j), path) = q.get()
        keypad_path[(key, keypad[i][j])] = path
        for move, di, dj in [("^", -1, 0), (">", 0, 1), ("v", 1, 0), ("<", 0, -1)]:
            ni, nj = i + di, j + dj
            if (
                ni >= 0
                and ni < 2
                and nj >= 0
                and nj < 3
                and (ni, nj) != (0, 0)
                and (ni, nj) not in visited
            ):
                visited.add((ni, nj))
                q.put(((ni, nj), path + move))


def keypad_robot2(seq, init):
    cur = init
    res = ""
    for c in seq:
        derive = keypad_path[(cur, c)] + "A"
        res += derive
        cur = c
    return res, cur


def keypad_robot(seq, init):
    cur = init
    res = ""
    derive_robot_cur = None
    for c in seq:
        derive = keypad_path[(cur, c)] + "A"
        r, derive_robot_cur = keypad_robot2(derive, "A" if derive_robot_cur is None else derive_robot_cur)
        res += r
        cur = c
    return res, cur


def numpad_robot(seq, init):
    cur = init
    res = ""
    derive_robot_cur = None
    for c in seq:
        derive = numpad_path[(cur, c)] + "A"
        r, derive_robot_cur = keypad_robot(derive, "A" if derive_robot_cur is None else derive_robot_cur)
        res += r
        cur = c
    return res

sum = 0
for line in sys.stdin:
    line = line.strip()
    seq = numpad_robot(line, "A")
    print(line, seq)
print(sum)
