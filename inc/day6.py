with open("input.txt", "r") as f:
    text = f.readlines()

grid = [list(line.strip()) for line in text]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            guardI = i
            guardJ = j
            break

d = "^"
print(guardI, guardJ, d)
visited = set()

def in_bounds(i, j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i])

def move_forward(i, j, d):
    if d == "^":
        return (i - 1, j)
    elif d == "v":
        return (i + 1, j)
    elif d == "<":
        return (i, j - 1)
    elif d == ">":
        return (i, j + 1)
    
def turn_right(d):
    if d == "^":
        return ">"
    elif d == ">":
        return "v"
    elif d == "v":
        return "<"
    elif d == "<":
        return "^"
    
obstacles = set()

def check_obstacle_cause_loop(i, j):

    gcopy = [row[:] for row in grid]
    gcopy[i][j] = "#"

    gi, gj = guardI, guardJ
    direction = d

    visited_states = set()
    visited_states.add((gi, gj, direction))

    while in_bounds(gi, gj):
        next_i, next_j = move_forward(gi, gj, direction)
        
        if not in_bounds(next_i, next_j) or gcopy[next_i][next_j] == "#":
            direction = turn_right(direction)
        else:
            gi, gj = next_i, next_j
            state = (gi, gj, direction)
            if state in visited_states:
                return True
            visited_states.add(state)
    
    return False


# while in_bounds(guardI, guardJ):
#     nextI, nextJ = move_forward(guardI, guardJ, d)

#     if grid[nextI][nextJ] == ".":
#         check_obstacle_cause_loop(nextI, nextJ)

#     if grid[nextI][nextJ] == "#":
#         d = turn_right(d)
    
#     else: 
#         visited.add((nextI, nextJ))
#         grid[nextI][nextJ] = "o"
#         grid[guardI][guardJ] = d
#         guardI, guardJ = nextI, nextJ

sol = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) != (guardI, guardJ) and grid[i][j] == ".":

            print("checking ", i, j)
            if check_obstacle_cause_loop(i, j):
                sol += 1

            print(sol)

print(sol)




# print(len(visited))