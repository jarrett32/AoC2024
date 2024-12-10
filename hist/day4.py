f = open("input.txt", "r")
text = f.readlines()

grid = [line.strip() for line in text]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0
word = "XMAS"
l = len(word) 

totalCount = 0


new_dir = [(-1, -1), (1, 1)]
new_dir_2 = [(-1, 1), (1, -1)]

def find_word(i, j):
    m1 = s1 = 0
    for dx, dy in new_dir:
        x, y = i + dx, j + dy
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        if grid[x][y] == "M":
            m1 += 1
        elif grid[x][y] == "S":
            s1 += 1

    if m1 != 1 or s1 != 1:
        return False

    m2 = s2 = 0
    for dx, dy in new_dir_2:
        x, y = i + dx, j + dy
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        if grid[x][y] == "M":
            m2 += 1
        elif grid[x][y] == "S":
            s2 += 1

    return m2 == 1 and s2 == 1
    

totalCount = 0

for i in range(rows):
    for j in range(cols):

        if grid[i][j] == "A":
            if find_word(i, j):
                totalCount += 1


print(totalCount)
