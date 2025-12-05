import time
import sys

with open("../input4.txt") as f:
    grid = [list(i) for i in f.read().strip().split("\n")]

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),            (0, 1),
    (1, -1), (1, 0), (1, 1)
]

RESET = "\x1b[0m"
RED   = "\x1b[31m"
BLUE  = "\x1b[34m"

MAP = {
    ".": "   ",
    "@": "███",
}

def render(grid, highlights=None):
    highlights = highlights or set()  # {(y, x), ...}

    sys.stdout.write("\x1b[H")  # cursor to top-left

    out = []

    for y, row in enumerate(grid):
        line = []
        for x, cell in enumerate(row):
            char = MAP[cell]

            if (y, x) in highlights:
                char = f"{BLUE}{char}{RESET}"

            line.append(char)

        out.append("".join(line) + "\n")

    sys.stdout.write("".join(out))
    sys.stdout.flush()

res = 0
print("\x1b[2J")  # clear screen
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
        #render(grid, toRemove)
    res += changes
    render(grid, toRemove)
    time.sleep(0.1)
    for y, x in toRemove:
        grid[y][x] = "."
    if changes == 0:
        break


print(res)
    
