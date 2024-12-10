from collections import deque


with open("input.txt", "r") as f:
    text = f.readlines()

rows = [list(map(int, line.strip())) for line in text if line.strip()]
print(rows)

rowLength = len(rows[0])
colLength = len(rows)

tHeads = []

for i in range(rowLength):
    for j in range(colLength):
        if rows[j][i] == 0:
            tHeads.append((i, j))

def getNeighbors(i, j):
    neighbors = []
    if i + 1 < rowLength:
        neighbors.append((i + 1, j))
    if i - 1 >= 0:
        neighbors.append((i - 1, j))
    if j + 1 < colLength:
        neighbors.append((i, j + 1))
    if j - 1 >= 0:
        neighbors.append((i, j - 1))
    return neighbors


tDict = {}

for tHead in tHeads:
    tDict[tHead] = []

def bfs(start_i, start_j):
    visited = set()
    visited.add((start_i, start_j))
    q = deque()
    q.append((start_i, start_j))
    found_nines = set()

    while q:
        i, j = q.popleft()
        h = rows[j][i]

        if h == 9:
            found_nines.add((i, j))
            continue

        next_height = h + 1
        for (ni, nj) in getNeighbors(i, j):
            if (ni, nj) not in visited and rows[nj][ni] == next_height:
                visited.add((ni, nj))
                q.append((ni, nj))

    return len(found_nines)

sol = 0
for tHead in tHeads:
    i, j = tHead
    score = bfs(i, j)
    sol += score

print(sol)