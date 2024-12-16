import sys

move_dir_map = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

input_moves = False
moves = ""
width, height = None, 0
grid = []
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
            width = len(line)
        grid.append([None] * width)
        for j, c in enumerate(line):
            if c == "@":
                robot_i, robot_j = height, j
            grid[height][j] = c
        height += 1


for move in moves:
    cur_i, cur_j = robot_i, robot_j
    di, dj = move_dir_map[move][0], move_dir_map[move][1]

    # no need to check grid bound since it's surrounded by '#'
    while grid[cur_i][cur_j] != '#' and grid[cur_i][cur_j] != '.':
        cur_i += di
        cur_j += dj

    if grid[cur_i][cur_j] == ".":
        grid[cur_i][cur_j] = grid[cur_i - di][cur_j - dj]
        grid[robot_i][robot_j] = "."
        grid[robot_i + di][robot_j + dj] = "@"
        robot_i += di
        robot_j += dj

sum = 0
for i in range(height):
    for j in range(width):
        if grid[i][j] == 'O':
            sum += 100 * i + j

print(sum)