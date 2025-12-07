with open("inputs/input7.txt") as f:
    lines = f.read().strip().split("\n")

lines = [list(i) for i in lines]

s = lines[0].index("S")

lines[1][s] = "|"

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


memo = {}
def allPaths(current):
    y, x = current
    
    if current in memo:
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
    return total


print(allPaths((1, lines[1].index("|"))))
print(res)
