import sys
from queue import Queue

blocks = []
dir = [(-1,0),(0,1),(1,0),(0,-1)]
width, height = 71,71
blocked = [[False for j in range(width)] for i in range(height)]
visited = [[False for j in range(width)] for i in range(height)]

for line in sys.stdin:
    (i,j) = (int(x) for x in line.split(','))
    blocks.append((i,j))

for k in range(1024):
    (i, j) = blocks[k]
    blocked[i][j] = True

q = Queue()
visited[0][0] = True
q.put((0, 0, 0))
while not q.empty():
    (step, i, j) = q.get()
    if i == height - 1 and j == width - 1:
        print(step)
        sys.exit(0)
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if ni >= 0 and ni < height and nj >= 0 and nj < width and not blocked[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = True
            q.put((step + 1, ni, nj)) 