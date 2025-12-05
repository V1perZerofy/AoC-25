with open("inputs/input4.txt") as f:
    grid = [list(i) for i in f.read().strip().split("\n")]



DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),            (0, 1),
    (1, -1), (1, 0), (1, 1)
]

res = 0
while True:
    changes = 0
    toRemove = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            current = grid[y][x]
            count = 0
            if current == "@":
                for dy, dx in DIRS:
                    ny, nx = y + dy, x + dx
                    
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                        neighbor = grid[ny][nx]
                        if neighbor == "@":
                            count += 1
                if count < 4:
                    changes += 1
                    toRemove.append((y, x))
    res += changes
    for y, x in toRemove:
        grid[y][x] = "."
    if changes == 0:
        break


print(res)
    
