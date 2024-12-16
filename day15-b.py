import sys

input_moves = False
moves = ""
width, height = None, 0
grid = []
clipboard = []
sum = 0

for line in sys.stdin:
    if line == "\n":
        input_moves = True
        continue
    if input_moves:
        moves += line.strip()
    else:
        line = line.strip()
        if width is None:
            width = len(line) * 2
        grid.append([None] * width)
        clipboard.append([None] * width)
        for j, c in enumerate(line):
            if c == "@":
                robot_i, robot_j = height, 2 * j
                grid[height][2 * j], grid[height][2 * j + 1] = "@", "."
            elif c == "O":
                grid[height][2 * j], grid[height][2 * j + 1] = "[", "]"
            else:
                grid[height][2 * j] = grid[height][2 * j + 1] = c
        height += 1

# these recursive functions are not efficient since there is no result memoization
# TODO: the code has a lot of duplicate logics, it could be refactored

def find_move_area_up(i, j):
    if grid[i][j] == ".":
        return True, set()
    if grid[i][j] == "#":
        return False, set()
    if grid[i][j] == "[":
        should_move_1, area_1 = find_move_area_up(i - 1, j)
        should_move_2, area_2 = find_move_area_up(i - 1, j + 1)
        return should_move_1 and should_move_2, area_1 | area_2 | {(i, j), (i, j + 1)}
    if grid[i][j] == "]":
        should_move_1, area_1 = find_move_area_up(i - 1, j)
        should_move_2, area_2 = find_move_area_up(i - 1, j - 1)
        return should_move_1 and should_move_2, area_1 | area_2 | {(i, j), (i, j - 1)}


def find_move_area_down(i, j):
    if grid[i][j] == ".":
        return True, set()
    if grid[i][j] == "#":
        return False, set()
    if grid[i][j] == "[":
        should_move_1, area_1 = find_move_area_down(i + 1, j)
        should_move_2, area_2 = find_move_area_down(i + 1, j + 1)
        return should_move_1 and should_move_2, area_1 | area_2 | {(i, j), (i, j + 1)}
    if grid[i][j] == "]":
        should_move_1, area_1 = find_move_area_down(i + 1, j)
        should_move_2, area_2 = find_move_area_down(i + 1, j - 1)
        return should_move_1 and should_move_2, area_1 | area_2 | {(i, j), (i, j - 1)}


def find_move_area_left(i, j):
    if grid[i][j] == ".":
        return True, set()
    if grid[i][j] == "#":
        return False, set()
    if grid[i][j] == "]":
        should_move, area = find_move_area_left(i, j - 2)
        return should_move, area | {(i, j), (i, j - 1)}


def find_move_area_right(i, j):
    if grid[i][j] == ".":
        return True, set()
    if grid[i][j] == "#":
        return False, set()
    if grid[i][j] == "[":
        should_move, area = find_move_area_right(i, j + 2)
        return should_move, area | {(i, j), (i, j + 1)}


def debug():
    for row in grid:
        for col in row:
            print(col, end="")
        print()


for move in moves:
    should_move, area = False, []
    if move == "^":
        should_move, area = find_move_area_up(robot_i - 1, robot_j)
        if should_move:
            for i, j in area:
                clipboard[i][j] = grid[i][j]
                grid[i][j] = "."
            for i, j in area:
                grid[i - 1][j] = clipboard[i][j]
            grid[robot_i][robot_j] = "."
            grid[robot_i - 1][robot_j] = "@"
            robot_i -= 1
    if move == ">":
        should_move, area = find_move_area_right(robot_i, robot_j + 1)
        if should_move:
            for i, j in area:
                clipboard[i][j] = grid[i][j]
                grid[i][j] = "."
            for i, j in area:
                grid[i][j + 1] = clipboard[i][j]
            grid[robot_i][robot_j] = "."
            grid[robot_i][robot_j + 1] = "@"
            robot_j += 1
    if move == "v":
        should_move, area = find_move_area_down(robot_i + 1, robot_j)
        if should_move:
            for i, j in area:
                clipboard[i][j] = grid[i][j]
                grid[i][j] = "."
            for i, j in area:
                grid[i + 1][j] = clipboard[i][j]
            grid[robot_i][robot_j] = "."
            grid[robot_i + 1][robot_j] = "@"
            robot_i += 1
    if move == "<":
        should_move, area = find_move_area_left(robot_i, robot_j - 1)
        if should_move:
            for i, j in area:
                clipboard[i][j] = grid[i][j]
                grid[i][j] = "."
            for i, j in area:
                grid[i][j - 1] = clipboard[i][j]
            grid[robot_i][robot_j] = "."
            grid[robot_i][robot_j - 1] = "@"
            robot_j -= 1

sum = 0
for i in range(height):
    for j in range(width):
        if grid[i][j] == "[":
            sum += i * 100 + j
print(sum)
