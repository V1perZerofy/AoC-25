import sys
import time

with open("../inputs/input7.txt") as f:
    lines = f.read().strip().split("\n")

lines = [list(i) for i in lines]
original = [row[:] for row in lines]

s = lines[0].index("S")

lines[1][s] = "|"

RESET = "\x1b[0m"
RED   = "\x1b[31m"
BLUE  = "\x1b[34m"

MAP = {
    ".": "   ",
    "^": "███",
    "S": "███",
} 

res = 0
for i in range(2, len(lines)):
    for j in range(len(lines[i])):
        if lines[i - 1][j] == "|":
            if lines[i][j] == ".":
                lines[i][j] = "|"
            elif lines[i][j] == "^":
                res += 1
                lines[i][j-1] = "|"
                lines[i][j+1] = "|"


def render(grid, highlights=None):
    highlights = highlights or set()
    
    sys.stdout.write("\x1b[H")

    out = []

    for y, row in enumerate(grid):
        line = []
        for x, cell in enumerate(row):
            char = MAP[cell]

            if (y, x) in highlights and char != "^":
                if highlights[(y, x)] < 2:
                    char = f"{RED}███{RESET}"

            line.append(char)

        out.append("".join(line) + "\n")

    sys.stdout.write("".join(out))
    sys.stdout.flush()

memo = {}
occs = {}
def allPaths(current):
    y, x = current
    
    if current in memo:
        occs[current] += 1
        return memo[current]

    if y == len(lines) - 1:
        return 1
    
    total = 0

    if lines[y+1][x] == "^":
        total += allPaths((y+1, x-1))
        total += allPaths((y+1, x+1))
    elif lines[y+1][x] == "|":
        total += allPaths((y+1, x))

    memo[current] = total
    occs[current] = 1
    render(original, occs)
    return total


print(allPaths((1, lines[1].index("|"))))
print(res)
