import sys
from queue import PriorityQueue

pq = PriorityQueue()  # (cost, i, j, dir)
width, height = None, 0
visited, grid = None, []
all_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start_i, start_j, end_i, end_j = None, None, None, None

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

visited = [
    [[False for dir in range(len(all_dir))] for j in range(width)] for i in range(height)
]

for dir in range(len(all_dir)):
    pq.put((1000, start_i, start_j, dir))

while True:
    if pq.empty():
        break
    cost, i, j, dir = pq.get()
    if visited[i][j][dir]:
        continue
    visited[i][j][dir] = True
    if i == end_i and j == end_j:
        print(cost)
        exit(0)
    for new_dir in range(len(all_dir)):
        if not visited[i][j][new_dir]:
            pq.put((cost + 1000, i, j, new_dir))
    new_i, new_j = i + all_dir[dir][0], j + all_dir[dir][1]
    if grid[new_i][new_j] == "." or grid[new_i][new_j] == "E":
        if not visited[new_i][new_j][dir]:
            pq.put((cost + 1, new_i, new_j, dir))
