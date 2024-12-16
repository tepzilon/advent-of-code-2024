import sys
from queue import PriorityQueue

pq = PriorityQueue()  # (cost, i, j, dir)
width, height = None, 0
dist, grid, prev = None, [], None
all_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start_i, start_j, end_i, end_j = None, None, None, None
tiles = set()

for line in sys.stdin:
    line = line.strip()
    if width is None:
        width = len(line)
    for j, c in enumerate(line):
        if c == "S":
            start_i, start_j = height, j
        if c == "E":
            end_i, end_j = height, j
    grid.append(line)
    height += 1

dist = [
    [[1000000000 for dir in range(len(all_dir))] for j in range(width)]
    for i in range(height)
]
prev = [
    [[set() for dir in range(len(all_dir))] for j in range(width)]
    for i in range(height)
]

for dir in range(len(all_dir)):
    pq.put((1000, start_i, start_j, dir))
    dist[start_i][start_j][dir] = 1000

while True:
    if pq.empty():
        break
    cost, i, j, dir = pq.get()
    for new_dir in range(len(all_dir)):
        if cost + 1000 < dist[i][j][new_dir]:
            dist[i][j][new_dir] = cost + 1000
            pq.put((cost + 1000, i, j, new_dir))
            prev[i][j][new_dir] = {(i, j, dir)}
        elif cost + 1000 == dist[i][j][new_dir]:
            prev[i][j][new_dir].add((i, j, dir))
    new_i, new_j = i + all_dir[dir][0], j + all_dir[dir][1]
    if grid[new_i][new_j] == "." or grid[new_i][new_j] == "E":
        if cost + 1 < dist[new_i][new_j][dir]:
            dist[new_i][new_j][dir] = cost + 1
            pq.put((cost + 1, new_i, new_j, dir))
            prev[new_i][new_j][dir] = {(i, j, dir)}
        elif cost + 1 == dist[new_i][new_j][dir]:
            prev[new_i][new_j][dir].add((i, j, dir))


def trace(i, j, dir):
    global tiles
    if i is None and j is None and dir is None:
        return
    tiles.add((i, j))
    for prev_i, prev_j, prev_dir in prev[i][j][dir]:
        trace(prev_i, prev_j, prev_dir)


for dir in range(len(all_dir)):
    trace(end_i, end_j, dir)

print(len(tiles))
