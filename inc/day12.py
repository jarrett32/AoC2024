from collections import deque

with open("input.txt", "r") as f:
    text = f.readlines()

grid = [list(line.strip()) for line in text]

def getNeighbors(i, j):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = []
    for di, dj in directions:
        ni, nj = i + di, j + dj
        neighbors.append((ni, nj))
    return neighbors


def bfs(i, j, visited):
    letter = grid[i][j]
    q = deque()
    q.append((i, j))
    visited.add((i, j))
    
    boundary_edges = set()
    area = 0
    while q:
        i, j = q.popleft()
        area += 1
        for (k, (ni, nj)) in enumerate(getNeighbors(i, j)):

            if k == 0: direction = 'down'
            elif k == 1: direction = 'up'
            elif k == 2: direction = 'right'
            else: direction = 'left'

            if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                perimeter += 1

            else: 
                if grid[ni][nj] == letter:

                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        q.append((ni, nj))

                else:
                    perimeter += 1

    return area,perimeter

visited = set()
total_cost = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) not in visited:
            area, perimeter = bfs(i, j, visited)
            total_cost += area * perimeter


print(total_cost)